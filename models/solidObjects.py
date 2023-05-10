from typing import overload
import numpy as np
import lib.features_parents as Features
from lib.object3D import Object3D
from lib.abstract import Instance


class WorldInfo(Instance):
    ID: str = "WorldInfo"
    COORDINATE_SYSTEM: str = Features.Features.COORDINATE_SYSTEM

    @staticmethod
    def get_instance() -> str:
        return WorldInfo.ID + Object3D.OPEN_SECTION \
            + Object3D.CLOSE_SECTION


class TexturedBackground(Features.TextureBase, Instance):
    ID: str = "TexturedBackground"
    SKYBOX: str = Features.Features.SKYBOX

    @staticmethod
    def get_instance() -> str:
        return f"{TexturedBackground.ID} {'{'} {'}'}\n"


class TexturedBackgroundLight(Features.TextureBase, Instance):
    ID: str = "TexturedBackgroundLight"
    CAST_SHADOWS: str = Features.Features.CASTSHADOWS

    @staticmethod
    def get_instance() -> str:
        return f"{TexturedBackgroundLight.ID} {'{'} {'}'}\n"


class ViewPoint(Object3D, Features.Positional3DFeatures, Instance):
    ID: str = "Viewpoint"

    @staticmethod
    def get_instance() -> str:
        return ViewPoint.ID \
            + Object3D.OPEN_SECTION \
            + f"{ViewPoint.ORIENTATION} -0.6003049099901187 0.5860248278486282 0.5442507842775618  " \
            f"2.12011455400134 \n" \
            f'{ViewPoint.POSITION} 0.6077590785915782 2.064357520835102 25.743958056170353 \n' \
            + Object3D.CLOSE_SECTION


class RectangleArena(Features.Basic3DFeatures, Instance):
    ID: str = "RectangleArena"
    CONTACT_MATERIAL: str = Features.Features.CONTACT_MATERIAL
    FLOOR_SIZE: str = Features.Features.FLOOR_SIZE

    @staticmethod
    def get_instance(width: int, height: int, object_count: int) -> str:
        return RectangleArena.ID \
            + Object3D.OPEN_SECTION \
            + Object3D.return_name(RectangleArena.ID, object_count) \
            + f"{RectangleArena.CONTACT_MATERIAL} \"concrete\" \n" \
            + f"{RectangleArena.ROTATION} 0 0 1 0\n" \
            + f"{RectangleArena.TRANSLATION} 0 0 0\n" \
            + f"{RectangleArena.FLOOR_SIZE} {width} {height} \n" \
            + Object3D.CLOSE_SECTION


class Floor(Features.Basic3DFeatures, Instance):
    ID: str = "Floor"
    SIZE: str = Features.Features.SIZE
    TILE_SIZE: str = Features.Features.TILE_SIZE
    CONTACT_MATERIAL: str = Features.Features.CONTACT_MATERIAL

    @staticmethod
    def get_instance(object_count: int, width: int, length: int, material: str = "concrete") -> str:
        return Floor.ID \
            + Object3D.OPEN_SECTION \
            + Object3D.return_name(id=Floor.ID, object_count=object_count) \
            + f"{Floor.CONTACT_MATERIAL} \"{material}\"\n" \
            f"{Floor.SIZE} {width} {length} \n" \
            "\tappearance Parquetry {\n"\
            "\t\ttype \"light strip\"\n" \
            "\t\tcolorOverride 1 0 1 \n"\
            "\t}\n" \
            + Object3D.CLOSE_SECTION


class Ceiling(Features.Basic3DFeatures, Instance):
    ID: str = "Ceiling"

    @staticmethod
    def get_instance(object_count: int, number_of_floor: int) -> str:
        return Ceiling.ID \
            + Object3D.OPEN_SECTION \
            + Object3D.return_name(Ceiling.ID, object_count) \
            + Object3D.return_rotation() \
            + Object3D.return_translation() \
            + Object3D.return_physics() \
            + Object3D.CLOSE_SECTION


class Transform(Features.Basic3DFeatures):
    ID: str = "Transform"
    SCALE: str = Features.Features.SCALE
    ROTATION_STEP: str = Features.Features.ROTATION_STEP
    CHILDREN: str = Features.Features.CHILDREN

    @staticmethod
    def open_transform_section() -> str:
        return f"{Transform.ID} {Object3D.OPEN_SECTION}" \
            "\tchildren [\n" \


    @staticmethod
    def open_transform_section_with_rotation(with_rotation) -> str:
        return f"{Transform.ID} {'{'} \n" \
            + Object3D.return_rotation() \
            + "\tchildren [\n" \


    @staticmethod
    def close_transform_section() -> str:
        return f"\t]\n{Object3D.CLOSE_SECTION}"


class Chair(Features.Basic3DFeatures, Instance):
    ID: str = "Chair"

    @staticmethod
    def get_instance(object_count: int, number_of_floor: int) -> str:
        return Chair.ID + Object3D.OPEN_SECTION \
            + Object3D.return_name(id=Chair.ID, object_count=object_count) \
            + Object3D.return_rotation(physics=True) \
            + Object3D.return_translation(physics=True) \
            + Object3D.return_physics() \
            + Object3D.CLOSE_SECTION


class Panel(Features.Basic3DFeatures, Instance):
    ID: str = "Panel"
    SIZE: str = Features.Features.SIZE
    PANELS_COUNT: str = Features.Features.PANELS_COUNT

    @staticmethod
    def get_instance(object_count: int, number_of_floor: int) -> str:
        return Panel.ID \
            + Object3D.OPEN_SECTION \
            + Object3D.return_name(id=Panel.ID, object_count=object_count) \
            + Object3D.return_rotation() \
            + Object3D.return_translation() \
            + Object3D.return_size() \
            + Object3D.return_panel_count() \
            + Object3D.CLOSE_SECTION


class WashingMachine(Features.Basic3DFeatures, Instance):
    ID: str = "WashingMachine"

    @staticmethod
    def get_instance(object_count: int, number_of_floor: int) -> str:
        return WashingMachine.ID \
            + Object3D.OPEN_SECTION \
            + Object3D.return_name(id=WashingMachine.ID, object_count=object_count) \
            + Object3D.return_rotation() \
            + Object3D.return_translation() \
            + Object3D.CLOSE_SECTION


class Bed(Features.Basic3DFeatures, Instance):
    ID: str = "Bed"

    @staticmethod
    def get_instance(object_count: int, number_of_floor: int) -> str:
        return Bed.ID \
            + Object3D.OPEN_SECTION \
            + Object3D.return_name(id=Bed.ID, object_count=object_count) \
            + Object3D.return_rotation() \
            + Object3D.return_translation() \
            + Object3D.CLOSE_SECTION


class Desk(Features.Basic3DFeatures, Instance):
    ID: str = "Desk"

    @staticmethod
    def get_instance(object_count: int, number_of_floor: int) -> str:
        return Desk.ID \
            + Object3D.OPEN_SECTION\
            + Object3D.return_name(id=Desk.ID, object_count=object_count) \
            + Object3D.return_rotation(physics=True) \
            + Object3D.return_translation(physics=True) \
            + Object3D.return_physics() \
            + Object3D.CLOSE_SECTION


class Fridge(Features.Basic3DFeatures, Features.HiddenFeatures, Instance):
    ID: str = "Fridge"

    @staticmethod
    def get_instance(object_count: int, number_of_floor: int) -> str:
        return Fridge.ID \
            + Object3D.OPEN_SECTION\
            + Object3D.return_name(id=Fridge.ID, object_count=object_count) \
            + Object3D.return_rotation() \
            + Object3D.return_translation() \
            + Object3D.CLOSE_SECTION


class Wall(Features.Basic3DFeatures, Features.AppearanceFeatures, Instance):
    ID: str = "Wall"

    @staticmethod
    def get_instance(object_count: int, number_of_floor: int) -> str:
        return Wall.ID \
            + Object3D.OPEN_SECTION\
            + Object3D.return_name(id=Wall.ID, object_count=object_count) \
            + Object3D.return_translation() \
            + Object3D.return_rotation() \
            + Object3D.return_size() \
            + "appearance  Roughcast { textureTransform TextureTransform { scale 2.4 1 } }" \
            + Object3D.CLOSE_SECTION


class Radiator(Features.Basic3DFeatures, Instance):
    ID: str = "Radiator"
    NUMBEROFFINS: str = Features.Features.NUMBEROFFINS

    @staticmethod
    def get_instance(object_count: int, number_of_floor: int) -> str:
        return Radiator.ID \
            + Object3D.OPEN_SECTION \
            + Object3D.return_name(id=Radiator.ID, object_count=object_count) \
            + Object3D.return_rotation() \
            + Object3D.return_translation() \
            + Object3D.return_number_of_pins() \
            + Object3D.CLOSE_SECTION


class Television(Features.Basic3DFeatures, Features.Display, Features.DisplayDevice, Instance):
    ID: str = "Television"

    @staticmethod
    def get_instance(object_count: int, number_of_floor: int) -> str:
        return Television.ID \
            + Object3D.OPEN_SECTION \
            + Object3D.return_name(id=Television.ID, object_count=object_count) \
            + Object3D.return_rotation() \
            + Object3D.return_translation() \
            + Object3D.CLOSE_SECTION


class Stairs(Features.Basic3DFeatures, Features.StepInfo, Instance):
    ID: str = "Stairs"

    @staticmethod
    def get_instance(object_count: int, number_of_floor: int) -> str:
        return Stairs.ID \
            + Object3D.OPEN_SECTION \
            + Object3D.return_name(id=Stairs.ID, object_count=object_count) \
            + Object3D.return_rotation() \
            + Object3D.return_translation() \
            + Object3D.return_number_of_step() \
            + Object3D.CLOSE_SECTION


class Book(Features.Basic3DFeatures, Features.Display, Instance):
    ID: str = "Book"

    @staticmethod
    def get_instance(object_count: int, number_of_floor: int) -> str:
        return Book.ID \
            + Object3D.OPEN_SECTION \
            + Object3D.return_name(id=Book.ID, object_count=object_count) \
            + Object3D.return_rotation() \
            + Object3D.return_translation() \
            + Object3D.CLOSE_SECTION


class Clock(Features.Basic3DFeatures, Instance):
    ID: str = "Clock"

    @staticmethod
    def get_instance(object_count: int, number_of_floor: int) -> str:
        return Clock.ID  \
            + Object3D.OPEN_SECTION \
            + Object3D.return_name(id=Clock.ID, object_count=object_count) \
            + Object3D.return_rotation() \
            + Object3D.return_translation() \
            + Object3D.CLOSE_SECTION


class LandscapePainting(Features.Basic3DFeatures, Features.Display, Instance):
    ID: str = "LandscapePainting"

    @staticmethod
    def get_instance(object_count: int, number_of_floor: int) -> str:
        return LandscapePainting.ID \
            + Object3D.OPEN_SECTION \
            + Object3D.return_name(LandscapePainting.ID, object_count=object_count) \
            + Object3D.return_rotation() \
            + Object3D.return_translation() \
            + Object3D.CLOSE_SECTION


class BathroomSink(Features.Basic3DFeatures, Instance):
    ID: str = "BathroomSink"

    @staticmethod
    def get_instance(object_count: int, number_of_floor: int) -> str:
        return BathroomSink.ID \
            + Object3D.OPEN_SECTION \
            + Object3D.return_name(id=BathroomSink.ID, object_count=object_count) \
            + Object3D.return_rotation() \
            + Object3D.return_translation() \
            + Object3D.CLOSE_SECTION


class Toilet(Features.Basic3DFeatures, Instance):
    ID: str = "Toilet"

    @staticmethod
    def get_instance(object_count: int, number_of_floor: int) -> str:
        return Toilet.ID \
            + Object3D.OPEN_SECTION \
            + Object3D.return_name(id=Toilet.ID, object_count=object_count) \
            + Object3D.return_rotation() \
            + Object3D.return_translation() \
            + Object3D.CLOSE_SECTION


class BathTube(Features.Basic3DFeatures, Instance):
    ID: str = "Bathtube"

    @staticmethod
    def get_instance(object_count: int, number_of_floor: int) -> str:
        return BathTube.ID \
            + Object3D.OPEN_SECTION \
            + Object3D.return_name(id=BathTube.ID, object_count=object_count) \
            + Object3D.return_rotation() \
            + Object3D.return_translation() \
            + Object3D.CLOSE_SECTION


class Cabinet(Features.Basic3DFeatures, Instance):
    ID: str = "Cabinet"

    @staticmethod
    def get_instance(object_count: int, number_of_floor: int) -> str:
        return Cabinet.ID \
            + Object3D.OPEN_SECTION \
            + Object3D.return_name(id=Cabinet.ID, object_count=object_count) \
            + Object3D.return_rotation() \
            + Object3D.return_translation() \
            + Object3D.CLOSE_SECTION


class Oven(Features.Basic3DFeatures, Instance):
    ID: str = "Oven"

    @staticmethod
    def get_instance(object_count: int, number_of_floor: int) -> str:
        return Oven.ID \
            + Object3D.OPEN_SECTION \
            + Object3D.return_name(id=Oven.ID, object_count=object_count) \
            + Object3D.return_rotation() \
            + Object3D.return_translation() \
            + Object3D.CLOSE_SECTION
