from models.world import World
import numpy as np
from lib.features_parents import Features
from lib.propertyGenerator import ObjectPropertiesGenerator

class Object3D:
    OPEN_SECTION = "{\n"
    CLOSE_SECTION = "}\n"
    
    @staticmethod
    def return_panel_count() -> str:
        count = ObjectPropertiesGenerator.create_panel_count()
        return f"{Features.PANELS_COUNT} {count} \n"
    
    
    @staticmethod
    def return_size() -> str:
        x, y, z =ObjectPropertiesGenerator.create_size()
        return f"{Features.SIZE} {x} {y} {z} \n"
    
    
    @staticmethod 
    def return_translation(physics: bool=False) -> str:
        x, y, z = ObjectPropertiesGenerator.create_translation(physics)
        return f"{Features.TRANSLATION} {x} {y} {z} \n"

    
    @staticmethod
    def return_rotation(physics: bool=False) -> str:
        x, y, z, angle = ObjectPropertiesGenerator.create_rotation(physics)
        return f"{Features.ROTATION} {x} {y} {z} {angle} \n"

    
    @staticmethod
    def return_name(id: str, object_count: int) -> str:
        return f"{Features.NAME} \"{id}({object_count})\" \n"
    
    @staticmethod
    def return_physics() -> str:
        return "\tphysics Physics {\n\t}\n"
    
    @staticmethod
    def return_enable_physics() -> str:
        return "\tenablePhysics TRUE\n"
    
    @staticmethod
    def return_number_of_pins() -> str:
        return f"{Features.NUMBEROFFINS} {ObjectPropertiesGenerator.return_random_int()} \n"
    
    @staticmethod
    def return_number_of_step() -> str:
        return f"{Features.STEP_SIZE} {ObjectPropertiesGenerator.return_random_int()} \n"
    
    @staticmethod
    def return_rotation_of_wall() -> str:
        x, y, z, angle = ObjectPropertiesGenerator.create_rotation()
        return f"\t{Features.ORIENTATION} {x} {y} {z} {angle} \n"
    
    @staticmethod
    def return_size_of_wall() -> str:
        return f"\t{Features.SIZE} 0.5 1 0.2 \n"
    
    @staticmethod
    def return_translation_of_wall() -> str:
        x, y, z = ObjectPropertiesGenerator.create_translation_wall()
        return f"\t{Features.TRANSLATION} {x} {y} {z} \n"
    
    @staticmethod
    def return_bounding_object() -> str:
        return "\tboundingObject Box { \n" \
            + "\t\tsize 0.1 0.1 0.1\n" \
            +  "}\n"
    
    