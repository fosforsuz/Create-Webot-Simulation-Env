import lib.solidObjects as solid


class MainElements:
    WORLD_INFO = solid.WorldInfo
    VIEW_POINT = solid.ViewPoint
    TEXTURED_BACKGROUND = solid.TexturedBackground
    TEXTURED_BACKGROUND_LIGHT = solid.TexturedBackgroundLight
    RECTANGLE_ARENA = solid.RectangleArena
    FLOOR = solid.Floor
    TRANSFORM = solid.Transform
    PANEL = solid.Panel
    BED = solid.Bed
    DESK = solid.Desk
    FRIDGE = solid.Fridge
    WALL = solid.Wall
    
    @staticmethod
    def __iterate_key__():
        for key, val in MainElements.__dict__.items():
            if not key.startswith("__"):
                yield key


    @staticmethod
    def __iterate_val__():
        for key, val in MainElements.__dict__.items():
            if not key.startswith("__"):
                yield val
                
    
    @staticmethod
    def __iterate_val_key__():
        for key, val in MainElements.__dict__.items():
            if not key.startswith("__"):
                yield val, key