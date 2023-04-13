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


class MainElements(Enum):
    WORLD_INFO = "WorldInfo"
    VIEW_POINT = "Viewpoint"
    TEXTURED_BACKGROUND = "TexturedBackground"
    TEXTURED_BACKGROUND_LIGHT = "TexturedBackgroundLight"
    RECTANGLE_ARENA = "RectangleArena"
    

class Chair(Enum):
    TRANSLATION = "translation"
    ROTATION = "rotation"
    

class Panel(Enum):
    TRANSLATION = "translation"
    ROTATION = "rotation"
    SIZE = "size"
    PANELS_COUNT = "panelsCount"
    
class PottedTree(Enum):
    TRANSLATION = "translation"
    ROTATION = "rotation"
    SIZE = "size"
    

class Bed(Enum):
    TRANSLATION = "translation"
    ROTATION = "rotation"
    SIZE = "size"
    

class SolidObjects:
    CHAIR = Chair
    PANEL = "Panel"
    POTTED_TREE = "PottedTree"
    BUNCH_OF_FLOWERS = "BunchOfFlowers"
    BOOK = "Book"
    DESK = "Desk"
    ROUND_TABLE = "RoundTable" 
    WASHING_MACHINE = "WashingMachine"
    BED = "Bed"
    FRIDGE = "Fridge"
    SOFA = "Sofa"
    OVEN = "Oven"
    ARMCHAIR = "Armchair"
    CABINET = "Cabinet"
    RADIATOR = "Radiator"
    WALL = "Wall"
    BATHTUBE = "Bathtube"
    TOILET = "Toilet"





class ObjectFeatures(Enum):
    COORDINATE_SYSTEM = "coordinateSystem"
    ORIENTATION = "orientation"
    TRANSLATION = "translation"
    POSITION = "position"
    FLOOR_SIZE = "floorSize"
    ROTATION = "rotation"
    NAME = "name"
    SIZE = "size"
    PANELS_COUNT = "panelsCount"
    HIDDEN_POSITION = "hidden position_"
    HIDDEN_ROTATION = "hidden rotation_"
    HIDDEN_TRANSLATION = "hidden translation_"
    HIDDEN_LINEAR_VELOCITY = "hidden linearVelocity_"
    HIDDEN_ANGULAT_VELOCITY = "hidden angularVelocity_"
    ROWS_HEIGHT = "rowsHeight"
    LAYOUT = "layout"
    RIGHT_SIDED_DOOR = "RightSidedDoor"
    LEFT_SIDED_DOOR = "LeftSidedDoor"