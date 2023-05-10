from enum import Enum
import pathlib


class FolderStructure(Enum):
    CURRENT_DIRECTORY = pathlib.Path.home()
    LIBRARY_PATH = "libraries"
    CONTROLLERS_PATH = "controllers"
    PLUGINS_PATH = "plugins"
    PROTOS_PATH = "protos"
    WORLDS_PATH = "worlds"    
