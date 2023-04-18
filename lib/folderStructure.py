from enum import Enum
from dataclasses import dataclass
import os


class FolderStructure(Enum):
    CURRENT_DIRECTORY = os.getcwd()
    LIBRARY_PATH = "libraries"
    CONTROLLERS_PATH = "controllers"
    PLUGINS_PATH = "plugins"
    PROTOS_PATH = "protos"
    WORLDS_PATH = "worlds"    
