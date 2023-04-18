from io import TextIOWrapper
from models.world import World
from models.mainElements import MainElements
from lib.external_libraries import create_ground
from lib.propertyGenerator import ObjectPropertiesGenerator
import numpy as np


class CreateEnv:

    def __init__(self, world):
        self.world: World = world

        self.constructor: list = ["CEILING", "FLOOR",
                                    "STAIRS", "RECTANGLE_ARENA", "WALL"]

        self.solidObjects: list = ["WORLD_INFO", "VIEW_POINT",
                                    "TEXTURED_BACKGROUND", "TEXTURED_BACKGROUND_LIGHT", "TRANSFORM"]

        self.objects: list = [item for item in MainElements.__iterate_key__(
        ) if item not in self.constructor + self.solidObjects]
        
        ObjectPropertiesGenerator.world = self.world

        self.object_counter: int = 0

    def open_file(self) -> TextIOWrapper:
        self.file = open(self.world.world_file_path, "a")
        return self.file

    def write_to_file(self, text: str) -> None:
        self.file.write(text)

    def increment_object_number(self) -> None:
        self.object_counter += 1

    def object_orientation(self, object_name: str, number_of_floor: int=0) -> str:
        self.increment_object_number()
        match object_name:
            case "WORLD_INFO":
                return MainElements.WORLD_INFO.get_instance()

            case "TEXTURED_BACKGROUND":
                return MainElements.TEXTURED_BACKGROUND.get_instance()

            case "TEXTURED_BACKGROUND_LIGHT":
                return MainElements.TEXTURED_BACKGROUND_LIGHT.get_instance()

            case "VIEW_POINT":
                return MainElements.VIEW_POINT.get_instance()

            case "RECTANGLE_ARENA":
                return MainElements.RECTANGLE_ARENA.get_instance(height=self.world.length, width=self.world.width, object_count=self.object_counter)

            case "FLOOR":
                return MainElements.FLOOR.get_instance(object_count=self.object_counter, width=self.world.width, length=self.world.length)

            case "CEILING":
                return MainElements.CEILING.get_instance(object_count=self.object_counter, number_of_floor=number_of_floor)

            case "PANEL":
                return MainElements.PANEL.get_instance(object_count=self.object_counter, number_of_floor=number_of_floor)
            
            case "FRIDGE":
                return MainElements.FRIDGE.get_instance(object_count=self.object_counter, number_of_floor=number_of_floor)

            case "BED":
                return MainElements.BED.get_instance(object_count=self.object_counter, number_of_floor=number_of_floor)

            case "DESK":
                return MainElements.DESK.get_instance(object_count=self.object_counter, number_of_floor=number_of_floor)

            case "CHAIR":
                return MainElements.CHAIR.get_instance(object_count=self.object_counter, number_of_floor=number_of_floor)

            case "RADIATOR":
                return MainElements.RADIATOR.get_instance(object_count=self.object_counter, number_of_floor=number_of_floor)

            case "TELEVISION":
                return MainElements.TELEVISION.get_instance(object_count=self.object_counter, number_of_floor=number_of_floor)

            case "BOOK":
                return MainElements.BOOK.get_instance(object_count=self.object_counter, number_of_floor=number_of_floor)

            case "CLOCK":
                return MainElements.CLOCK.get_instance(object_count=self.object_counter, number_of_floor=number_of_floor)

            case "LANDSCAPE_PAINTING":
                return MainElements.LANDSCAPE_PAINTING.get_instance(object_count=self.object_counter, number_of_floor=number_of_floor)

            case "BATHROOM_SINK":
                return MainElements.BATHROOM_SINK.get_instance(object_count=self.object_counter, number_of_floor=number_of_floor)

            case "TOILET":
                return MainElements.TOILET.get_instance(object_count=self.object_counter, number_of_floor=number_of_floor)

            case "BATH_TUBE":
                return MainElements.BATH_TUBE.get_instance(object_count=self.object_counter, number_of_floor=number_of_floor)

            case "CABINET":
                return MainElements.CABINET.get_instance(object_count=self.object_counter, number_of_floor=number_of_floor)

            case "OVEN":
                return MainElements.OVEN.get_instance(object_count=self.object_counter, number_of_floor=number_of_floor)
            case "CREATE_GROUND":
                return create_ground

    def create_world_base(self) -> None:
        main_elements: list = ["WORLD_INFO", "VIEW_POINT",
                                "TEXTURED_BACKGROUND", "TEXTURED_BACKGROUND_LIGHT", "FLOOR", "CREATE_GROUND"]
        for element in main_elements:
            text = self.object_orientation(element)
            self.write_to_file(text=text)

        del main_elements
        del text
    
    
    def create_elements(self, number_of_floor: int) -> None:
        random_object = np.random.choice(self.objects)
        text = self.object_orientation(random_object, number_of_floor)
        self.write_to_file(text=text)
    


    def create_world(self, number_of_floor: int) -> None:
        iteration_count = ObjectPropertiesGenerator.return_object_number()
        for i in range(0, iteration_count):
            self.create_elements(number_of_floor)
    
    
    def create_ceiling(self, number_of_floor: int) -> None:
        self.write_to_file(text=self.object_orientation("CEILING", number_of_floor))
