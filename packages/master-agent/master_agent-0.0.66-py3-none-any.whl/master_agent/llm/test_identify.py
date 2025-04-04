import os
from dotenv import load_dotenv
from .identify import TileIdentifier
from .client import LlmClient
from envs.complexEnv import ComplexEnv
from envs.noLavaEnv import NoLavaEnv 

def test_tile_identifier_complex():
    load_dotenv()

    llm_api_key = os.getenv('LLM_API_KEY')
    assert llm_api_key != None
    llm_base_url = os.getenv('LLM_BASE_URL')
    assert llm_base_url != None
    llm_model = os.getenv('LLM_MODEL')
    assert llm_model != None

    llm_client = LlmClient(llm_api_key, llm_model, llm_base_url)

    identifier = TileIdentifier(llm_client)

    env = ComplexEnv(render_mode='rgb_array', highlight=False) # Removing highlight for accurate tileset representation
    env.reset()

    unidentified_tileset = identifier.parse_tileset(env.render())
    
    identifier.validate_unidentified_tileset(unidentified_tileset, env)

    tileset = identifier.identify_tiles(unidentified_tileset)

    VALID_TILE_NAMES = [ "Goal", "Empty", "Agent", "YellowKey", "YellowDoor", "Wall", "Lava"]
    
    tile_names = [tile.name for tile in tileset.tiles]
    assert set(tile_names) == set(VALID_TILE_NAMES), f"Tile names {tile_names} do not match valid tile names {VALID_TILE_NAMES}"
    
def test_tile_identifier_no_lava():
    load_dotenv()

    llm_api_key = os.getenv('LLM_API_KEY')
    assert llm_api_key != None
    llm_base_url = os.getenv('LLM_BASE_URL')
    assert llm_base_url != None
    llm_model = os.getenv('LLM_MODEL')
    assert llm_model != None

    llm_client = LlmClient(llm_api_key, llm_model, llm_base_url)

    identifier = TileIdentifier(llm_client)

    env = NoLavaEnv(render_mode='rgb_array', highlight=False) # Removing highlight for accurate tileset representation
    env.reset()

    unidentified_tileset = identifier.parse_tileset(env.render())
    
    identifier.validate_unidentified_tileset(unidentified_tileset, env)

    tileset = identifier.identify_tiles(unidentified_tileset)
    
    VALID_TILE_NAMES = [ "Goal", "Empty", "Agent", "YellowKey", "YellowDoor", "Wall"]
    
    tile_names = [tile.name for tile in tileset.tiles]
    assert set(tile_names) == set(VALID_TILE_NAMES), f"Tile names {tile_names} do not match valid tile names {VALID_TILE_NAMES}"