from typing import overload
from features import Features
from abstract import Instance

class Object3D(Instance):
    
    @staticmethod 
    def create_translation(x: float, y: float, z: float) -> str:
        return f"{Features.TRANSLATION} {x} {y} {z} \n"

    
    @staticmethod
    def create_rotation(self, x: float, y: float, z: float, angle: float) -> str:
        return f"{Features.ROTATION} {x} {y} {z} {angle} \n"

    
    @staticmethod
    def create_name(name: str) -> str:
        return f"{Features.NAME} \"{name}\" \n"


    @staticmethod
    @overload
    def get_instance() -> str:
        # This is the overload for the default get_instance() method
        pass
        
    
