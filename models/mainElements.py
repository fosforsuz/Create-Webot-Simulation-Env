import models.solidObjects as solid
from lib.utility import external_libraries
from abc import ABC


class SceneSettings:
    WORLD_INFO = solid.WorldInfo
    VIEW_POINT = solid.ViewPoint
    TEXTURED_BACKGROUND = solid.TexturedBackground
    TEXTURED_BACKGROUND_LIGHT = solid.TexturedBackgroundLight
    TRANSFORM = solid.Transform
    GROUND = external_libraries.create_ground
    
    @staticmethod
    def __iterate_key__():
        for key, val in SceneSettings.__dict__.items():
            if not key.startswith("__"):
                yield key


    @staticmethod
    def __iterate_val__():
        for key, val in SceneSettings.__dict__.items():
            if not key.startswith("__"):
                yield val
                
    
    @staticmethod
    def __iterate_val_key__():
        for key, val in SceneSettings.__dict__.items():
            if not key.startswith("__"):
                yield val, key


class BuildingMaterial:
    WALL = solid.Wall
    RECTANGLE_ARENA = solid.RectangleArena
    STAIRS = solid.Stairs
    CEILING = solid.Ceiling
    FLOOR = solid.Floor
    
    @staticmethod
    def __iterate_key__():
        for key, val in BuildingMaterial.__dict__.items():
            if not key.startswith("__"):
                yield key


    @staticmethod
    def __iterate_val__():
        for key, val in BuildingMaterial.__dict__.items():
            if not key.startswith("__"):
                yield val
                
    
    @staticmethod
    def __iterate_val_key__():
        for key, val in BuildingMaterial.__dict__.items():
            if not key.startswith("__"):
                yield val, key