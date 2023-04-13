import numpy as np
from world import World
from lib.solidObjects import MainElements
import utility


class CreateEnv:
    
    def __init__(self, world):
        self.world: World = world
        self.create_world()
        
    def create_world(self):
        utility.create_main_structure(
            self.world.world_file_path, MainElements.WORLD_INFO.get_instance())
        utility.create_main_structure(
            self.world.world_file_path, MainElements.VIEW_POINT.get_instance())
        utility.create_main_structure(
            self.world.world_file_path, MainElements.TEXTURED_BACKGROUND.get_instance())
        utility.create_main_structure(
            self.world.world_file_path, MainElements.TEXTURED_BACKGROUND_LIGHT.get_instance())
        utility.create_main_structure(self.world.world_file_path,
                                        MainElements.FLOOR.get_instance(width=self.world.width,
                                                                        length=self.world.length,
                                                                        name="Floor"
                                                                    ))
