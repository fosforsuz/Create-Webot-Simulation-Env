import models.solidObjects as solid
from abc import ABC


class MainElements:
    WORLD_INFO = solid.WorldInfo
    VIEW_POINT = solid.ViewPoint
    TEXTURED_BACKGROUND = solid.TexturedBackground
    TEXTURED_BACKGROUND_LIGHT = solid.TexturedBackgroundLight
    TRANSFORM = solid.Transform
    PANEL = solid.Panel
    BED = solid.Bed
    DESK = solid.Desk
    FRIDGE = solid.Fridge
    RADIATOR = solid.Radiator
    TELEVISION = solid.Television
    BOOK = solid.Book
    CLOCK = solid.Clock
    LANDSCAPE_PAINTING = solid.LandscapePainting
    BATHROOM_SINK = solid.BathroomSink
    TOILET = solid.Toilet
    BATH_TUBE = solid.BathTube
    CABINET = solid.Cabinet
    OVEN = solid.Oven
    CHAIR = solid.Chair
    
    WALL = solid.Wall
    RECTANGLE_ARENA = solid.RectangleArena
    STAIRS = solid.Stairs
    CEILING = solid.Ceiling
    FLOOR = solid.Floor

    
    
    
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
