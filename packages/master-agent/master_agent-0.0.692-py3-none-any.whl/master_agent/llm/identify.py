import json
import re
import cv2
import imageio
from .client import LlmClient
from .utils import strip_code_fences
import numpy as np
from minigrid.core.world_object import WorldObj
from minigrid.minigrid_env import MiniGridEnv
from minigrid.core.constants import OBJECT_TO_IDX, COLOR_NAMES
import base64
from importlib import resources

# Constants
DATASET_IMG_NAMES = ['empty.png', 'agent.png', 'box.png', 'key.png', 'door.png', 'wall.png', 'lava.png', 'goal.png']

VALID_INDIFICATION_OBJECTS = OBJECT_TO_IDX.keys()

OBJECTS_WITH_COLORS = ["door", "key", "ball", "box"]

VALID_INDIFICATION_COLORS = COLOR_NAMES

class UnidentifiedTile:
    def __init__(self, img: np.ndarray, positions: list[tuple[int, int]], size: tuple[int, int]):
        self.img = img
        self.positions = positions
        self.size = size
        

class UnidentifiedTileset:
    def __init__(self, tiles: list[UnidentifiedTile]):
        self.tiles = tiles
        self.width, self.height = self.get_grid_dimensions()

    def get_grid_dimensions(self) -> tuple[int, int]:
        """Get the dimensions of the grid based on the min and max positions of the tiles."""
        if not self.tiles:
            raise ValueError("Tileset is empty. Cannot determine grid dimensions.")

        min_x = min(pos[0] for tile in self.tiles for pos in tile.positions)
        max_x = max(pos[0] for tile in self.tiles for pos in tile.positions)
        min_y = min(pos[1] for tile in self.tiles for pos in tile.positions)
        max_y = max(pos[1] for tile in self.tiles for pos in tile.positions)

        grid_width = max_x - min_x + 1
        grid_height = max_y - min_y + 1

        return grid_width, grid_height

class Tile(UnidentifiedTile):
    def __init__(self, unid_tile: UnidentifiedTile, name: str, world_obj: WorldObj | None = None):
        super().__init__(unid_tile.img, unid_tile.positions, unid_tile.size)
        self.name = name
        self.world_obj = world_obj

class Tileset:
    def __init__(self, tiles: list[Tile]):
        self.tiles = tiles
        self.width, self.height = self.get_grid_dimensions()

    def get_grid_dimensions(self) -> tuple[int, int]:
        """Get the dimensions of the grid based on the min and max positions of the tiles."""
        if not self.tiles:
            raise ValueError("Tileset is empty. Cannot determine grid dimensions.")

        min_x = min(pos[0] for tile in self.tiles for pos in tile.positions)
        max_x = max(pos[0] for tile in self.tiles for pos in tile.positions)
        min_y = min(pos[1] for tile in self.tiles for pos in tile.positions)
        max_y = max(pos[1] for tile in self.tiles for pos in tile.positions)

        grid_width = max_x - min_x + 1
        grid_height = max_y - min_y + 1

        return grid_width, grid_height

class TileIdentifier:
    def __init__(self, llm_client: LlmClient):
        self.llm_client = llm_client

    def parse_tileset(self, img: np.ndarray) -> UnidentifiedTileset:
        if len(img.shape) != 3 or img.shape[2] != 3:
            raise ValueError("img must be a 3-dimensional array with 3 channels (RGB).")
        
        img_h, img_w = img.shape[:2]

        tile_w, tile_h = self._get_tilesize(img, img_w, img_h)

        tiles_arr = self._get_tiles(img, img_w, img_h, tile_w, tile_h)

        unique_tiles = np.unique(tiles_arr.reshape(-1, 32, 32, 3), axis=0)

        tile_positions = {}
        for tile_id, tile in enumerate(unique_tiles):
            tile_positions[tile_id] = []
            for row_idx, row in enumerate(tiles_arr):
                for col_idx, grid_tile in enumerate(row):
                    if np.array_equal(grid_tile, tile):
                        tile_positions[tile_id].append((row_idx, col_idx))
        
        unidentified_tiles = []
        for tile_id, positions in tile_positions.items():
            tile = unique_tiles[tile_id]
            unidentified_tiles.append(UnidentifiedTile(tile, positions, (tile_w, tile_h)))

        return UnidentifiedTileset(unidentified_tiles)

    def validate_unidentified_tileset(self, tileset: UnidentifiedTileset, env: MiniGridEnv) -> None:
        """Validate the unidentified tileset against the Minigrid environment.
        
        Args:
            tileset: UnidentifiedTileset to validate
            env: Minigrid environment to validate against
            
        Returns:
            None
        
        Raises:
            ValueError: If the tileset dimensions do not match the environment grid dimensions
            ValueError: If the tile size does not match the environment tile size
        """
        if tileset.width != env.grid.width or tileset.height != env.grid.height:
            raise ValueError("Tileset dimensions do not match environment grid dimensions.")
        
        if tileset.tiles[0].size[0] != env.tile_size or tileset.tiles[0].size[1] != env.tile_size:
            raise ValueError("Tile size does not match environment tile size.")

    def _get_tilesize(self, img: np.ndarray, img_w: int, img_h: int) -> tuple[int, int]:
        cv_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Find bounding boxes of the smallest repetitive element (tile size)
        tile_width, tile_height = None, None
        for contour in contours:
            _, _, w, h = cv2.boundingRect(contour)
            # Only accept square bounding boxes
            if w == h and img_w % w == 0 and img_h % h == 0:
                tile_width, tile_height = w, h

        # Check if tile size was found
        if tile_width is None or tile_height is None:
            raise ValueError("Could not find bounding box of the smallest repetitive element.")

        return tile_width, tile_height
    
    def _get_tiles(self, img: np.ndarray, img_w: int, img_h: int, tile_w: int, tile_h: int) -> np.ndarray:
        tiles_arr = []
        for y in range(0, img_h, tile_h):
            row = []
            for x in range(0, img_w, tile_w):
                tile = img[y:y+tile_h, x:x+tile_w]
                row.append(tile)
            tiles_arr.append(row)

        return np.array(tiles_arr)
    
    def identify_tiles(self, unidentified_tileset: UnidentifiedTileset) -> Tileset:
        """Identify tiles in the unidentified tileset using the LLM.
        
        Args:
            tileset: UnidentifiedTileset to identify
        Returns:
            Tileset: Identified tileset
        """
        if not unidentified_tileset.tiles:
            raise ValueError("Tileset is empty. Cannot identify tiles.")
        
        # load code references
        code_references = []

        try:
            with resources.files('master_agent.llm.dataset.files').joinpath('minigrid-actions.py').open('r') as f:
                actions_code = f.read()
                code_references.append(
                    {"type": "text", "text": "<code>\nminigrid-actions.py\n" + actions_code+ "\n</code>"}
                )
        except Exception as e:
            print(f"Error loading minigrid-actions.py: {e}")

        try:
            with resources.files('master_agent.llm.dataset.files').joinpath('minigrid-constants.py').open('r') as f:
                constants_code = f.read()
                code_references.append(
                    {"type": "text", "text": "<code>\nminigrid-constants.py\n" + constants_code+ "\n</code>"}
                )
        except Exception as e:
            print(f"Error loading minigrid-constants.py: {e}")

        # load dataset references
        img_validation_chat_history = []
        
        # Get all image files from the dataset
        dataset_path = resources.files('master_agent.llm.dataset.imgs')
        
        # Iterate through all PNG files in the dataset
        for img_name in DATASET_IMG_NAMES:
            try:
                # Read the image file using resources API
                with dataset_path.joinpath(img_name).open('rb') as f:
                    img_data = f.read()
                    img_base64 = base64.b64encode(img_data).decode('utf-8')
                
                # Add the image to the chat history
                img_validation_chat_history.extend([
                    {
                        "role": "user",
                        "content": [{
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{img_base64}",
                            }
                        }]
                    },
                    {
                        "role": "assistant",
                        "content": [{"type": "text", "text": f"This is a {img_name}"}]
                    },
                    {
                        "role": "user",
                        "content": [{"type": "text", "text": f"Correct!"}]
                    },
                    {
                        "role": "assistant",
                        "content": [{"type": "text", "text": f"Thank you!"}]
                    }
                ])
            except Exception as e:
                print(f"Error loading image {img_name}: {e}")

        identified_tiles = []

        for tile in unidentified_tileset.tiles:
            # Convert numpy array to PNG image and encode as base64 string
            buffer = imageio.v3.imwrite("<bytes>", tile.img, extension=".png")
            img_base64 = base64.b64encode(buffer).decode('utf-8')
        
            messages = [
                {
                    "role": "system",
                    "content": [{"type": "text", "text": f"You are a vision model classifying tiles based on references. Identify the first image using the python files provided in <code> and previous correct identications to label the current user prompt."}]
                }
            ] + img_validation_chat_history + [
                {
                    "role": "user",
                    "content": (
                        code_references +
                        [
                            {
                                "type": "text", 
                                "text": f'Identify this image based on your previous correct identifications\nOutput format:\n{{\nobject_type: "...",\nobject_color: "..."\n}}'
                            }, 
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/png;base64,{img_base64}",
                                }
                            }
                        ]
                    )
                }
            ]

            res_text = strip_code_fences(self.llm_client.complete(messages))
            res_json = json.loads(res_text.replace("object_type:", '"object_type":').replace("object_color:", '"object_color":'))
            object_type = str(res_json.get("object_type"))
            object_color = str(res_json.get("object_color"))
            
            if object_type is None or object_type not in VALID_INDIFICATION_OBJECTS:
                raise ValueError(f"Invalid object type: {object_type}")
            if object_type in OBJECTS_WITH_COLORS:
                if object_color is None or object_color not in VALID_INDIFICATION_COLORS:
                    raise ValueError(f"Invalid object color: {object_color}")
                world_obj = WorldObj(object_type, object_color)
                name = f"{object_color.capitalize()}{object_type.capitalize()}"
                identified_tiles.append(Tile(tile, name, world_obj))
            else:
                identified_tiles.append(Tile(tile, object_type.capitalize()))
        
        return Tileset(identified_tiles)