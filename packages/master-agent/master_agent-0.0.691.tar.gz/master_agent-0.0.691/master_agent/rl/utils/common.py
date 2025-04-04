from stable_baselines3 import PPO
from stable_baselines3.common.torch_layers import BaseFeaturesExtractor
import torch
import torch.nn as nn 
import gymnasium as gym
from minigrid.wrappers import ImgObsWrapper, ActionBonus, NoDeath
from gymnasium import spaces
import numpy as np