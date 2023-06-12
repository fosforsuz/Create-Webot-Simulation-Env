from models.world import World
import numpy as np
import time

np.random.seed(int(time.time()))

class ObjectPropertiesGenerator:
    world: World
    
    @staticmethod
    def create_translation(physics: bool=False) -> tuple:

        x = np.random.randint(-1/2 * ObjectPropertiesGenerator.world.width + 0.5 , 1/2 * ObjectPropertiesGenerator.world.width - 0.5)
        y = np.random.randint(-1/2 * ObjectPropertiesGenerator.world.length + 0.5 , 1/2 * ObjectPropertiesGenerator.world.length - 0.5)
        z = 0.1
        if physics:
            z = np.random.randint(0, 4)
        return x, y, z
    
    @staticmethod
    def create_translation_wall() -> tuple:
        x = np.random.randint(-1/2 * ObjectPropertiesGenerator.world.width + 0.5 , 1/2 * ObjectPropertiesGenerator.world.width - 0.5)
        y = np.random.randint(-1/2 * ObjectPropertiesGenerator.world.length + 0.5 , 1/2 * ObjectPropertiesGenerator.world.length - 0.5)
        z = 0
        return x, y, z
    
    
    @staticmethod
    def create_rotation(physics: bool=False) -> tuple:
        x = np.random.uniform(-3, 3)
        y = np.random.uniform(-3, 3)
        z = np.random.uniform(-3, 3)
        angle = np.random.uniform(-3, 3)
        return x, y, z, angle


    
    @staticmethod
    def create_panel_count() -> int:
        return np.random.randint(1, 10)
    
    
    @staticmethod
    def create_size() -> tuple:
        x = np.random.uniform(0, 2)
        y = np.random.uniform(0, 2)
        z = np.random.uniform(0, 2)
        return x, y, z
    
    
    @staticmethod
    def return_random_int() -> int:
        return np.random.randint(0, 15)
    
    
    @staticmethod
    def return_object_number() -> int:
        world_size = ObjectPropertiesGenerator.world.width * ObjectPropertiesGenerator.world.length
        return np.random.randint(world_size * 0.30, world_size * 0.50)