from io import TextIOWrapper
from models.world import World
from models.mainElements import SceneSettings, BuildingMaterial
from models.homeStuff import HomeStuff
from lib.external_libraries import create_ground
from lib.propertyGenerator import ObjectPropertiesGenerator
import numpy as np


class CreateEnv:
    def __init__(self, world: World):
        self.world: World = world
        self.object_count: int = 0
        ObjectPropertiesGenerator.world = world
        self.open_file()
        self.get_object_names()
        self.create_total_object_count = np.random.randint(world.length * world.width * 0.3, world.length * world.width * 0.5)
    
    def get_building_material(self, object_id: str, number_of_floor:int) -> str:
        match object_id:
            case "WORLD_INFO":
                return SceneSettings.WORLD_INFO.get_instance()
            case "VIEW_POINT":
                return SceneSettings.VIEW_POINT.get_instance()
            case "TEXTURED_BACKGROUND":
                return SceneSettings.TEXTURED_BACKGROUND.get_instance()
            case "TEXTURED_BACKGROUND_LIGHT":
                return SceneSettings.TEXTURED_BACKGROUND_LIGHT.get_instance()
            case "GROUND":
                return SceneSettings.GROUND
            case "WALL":
                return BuildingMaterial.WALL.get_instance(object_count=self.object_count, number_of_floor=number_of_floor)
            case "RECTANGLE_ARENA":
                return BuildingMaterial.RECTANGLE_ARENA.get_instance(width=self.world.width, height=self.world.length, object_count=self.object_count)
            case "STAIRS":
                return BuildingMaterial.STAIRS.get_instance(object_count=self.object_count, number_of_floor=number_of_floor)
            case "CEILING":
                return BuildingMaterial.CEILING.get_instance(object_count=self.object_count, number_of_floor=number_of_floor)
            case "FLOOR":
                return BuildingMaterial.FLOOR.get_instance(width=self.world.width, length=self.world.length,object_count=self.object_count)
            case "PHOTO_FRAME":
                return HomeStuff.PHOTO_FRAME.get_instance(object_count=self.object_count)
            case "CHAIR":
                return HomeStuff.CHAIR.get_instance(object_count=self.object_count)
            case "OFFICE_CHAIR":
                return HomeStuff.OFFICE_CHAIR.get_instance(object_count=self.object_count)
            case "WOODEN_CHAIR":
                return HomeStuff.WOODEN_CHAIR.get_instance(object_count=self.object_count)
            case "BARBECUE":
                return HomeStuff.BARBECUE.get_instance(object_count=self.object_count)
            case "GNOME": 
                return HomeStuff.GNOME.get_instance(object_count=self.object_count)
            case "WATERING_CAN":
                return HomeStuff.WATERING_CAN.get_instance(object_count=self.object_count)
            case "WHEEL_BARROW":
                return HomeStuff.WHEEL_BARROW.get_instance(object_count=self.object_count)
            case "MEDICINE_BOTTLE":
                return HomeStuff.MEDICINE_BOTTLE.get_instance(object_count=self.object_count)
            case "FLOOR_LIGHT":
                return HomeStuff.FLOOR_LIGHT.get_instance(object_count=self.object_count)
            case "SOFA":
                return HomeStuff.SOFA.get_instance(object_count=self.object_count)
            case "ARM_CHAIR":
                return HomeStuff.ARM_CHAIR.get_instance(object_count=self.object_count)
            case "MIRROR":
                return HomeStuff.MIRROR.get_instance(object_count=self.object_count)
            case "BUNCH_OF_FLOWERS":
                return HomeStuff.BUNCH_OF_FLOWERS.get_instance(object_count=self.object_count)
            case "FLOWER_POT":
                return HomeStuff.FLOWER_POT.get_instance(object_count=self.object_count)
            case "DESK":
                return HomeStuff.DESK.get_instance(object_count=self.object_count)
            case "ROUND_TABLE":
                return HomeStuff.ROUND_TABLE.get_instance(object_count=self.object_count)
            case "OFFICE_TELEPHONE":
                return HomeStuff.OFFICE_TELEPHONE.get_instance(object_count=self.object_count)
            case "POTTED_TREE":
                return HomeStuff.POTTED_TREE.get_instance(object_count=self.object_count)

    def get_object_names(self):
        self.scene_settings = [x for x in SceneSettings.__iterate_key__()]
        self.building_materials = [x for x in BuildingMaterial.__iterate_key__()]
        self.home_stuff = [x for x in HomeStuff.__iterate_key__()]

    def open_file(self):
        self.file = open(self.world.world_file_path, 'a')

    def write_to_file(self, text: str):
        self.file.write(text)
    
    
    def close_file(self):
        self.file.close()
    
    def create_scene_settings(self):
        for material in self.scene_settings:
            if material != "TRANSFORM":
                self.write_to_file(self.get_building_material(material, 0))
                self.object_count += 1
        self.write_to_file(self.get_building_material("FLOOR", 0))
    
    
    def create_materials(self):
        counter: int = 0
        while counter < self.create_total_object_count:
            material = self.home_stuff[np.random.randint(0, len(self.home_stuff))]
            self.write_to_file(self.get_building_material(material, 0))
            self.object_count += 1
            counter += 1
    


