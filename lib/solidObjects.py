from typing import overload
import numpy as np
import features as features
from object3D import Object3D
from lib.abstract import Instance


class WorldInfo(Instance):
    ID: str = "WorldInfo"
    COORDINATE_SYSTEM: str = features.Features.COORDINATE_SYSTEM

    @staticmethod
    def get_instance() -> str:
        return WorldInfo.ID + "{\n" \
            + WorldInfo.COORDINATE_SYSTEM \
            + "}\n"


class ViewPoint(Object3D, features.Positional3DFeatures):
    ID: str = "Viewpoint"

    @staticmethod
    def get_instance() -> str:
        return f"{ViewPoint.ID} {'{'}\n" \
               f"{ViewPoint.ORIENTATION} 0.06055435408039591 -0.033257383193768815 -0.9976107039647324 " \
               f"3.153653224698355 \n" \
               f'{ViewPoint.POSITION} 13.648152950347704 3.748782732166771 1.0662266522655417 \n' \
               "}\n"


class TexturedBackground(features.TextureBase, Instance):
    ID: str = "TexturedBackground"

    @staticmethod
    def get_instance() -> str:
        return f"{TexturedBackground.ID} {'{'} {'}'}\n"


class TexturedBackgroundLight(features.TextureBase, Instance):
    ID: str = "TexturedBackgroundLight"

    @staticmethod
    def get_instance() -> str:
        return f"{TexturedBackgroundLight.ID} {'{'} {'}'}\n"


class RectangleArena(features.features.Basic3DFeatures, Object3D):
    ID: str = "RectangleArena"
    CONTACT_MATERIAL: str = features.Features.CONTACT_MATERIAL
    FLOOR_SIZE: str = features.Features.FLOOR_SIZE

    @staticmethod
    @overload
    def get_instance(width: int, height: int, name: str) -> str:
        return f"{RectangleArena.ID} {'{'}\n" \
               f"{RectangleArena.NAME} \"{name}\" \n" \
               f"{RectangleArena.CONTACT_MATERIAL} \"concrete\" \n" \
               f"{RectangleArena.FLOOR_SIZE} {width} {height} \n" \
               "}\n"


class Floor(features.Basic3DFeatures, Object3D):
    ID: str = "Floor"
    SIZE: str = features.Features.SIZE
    TILE_SIZE: str = features.Features.TILE_SIZE
    CONTACT_MATERIAL: str = features.Features.CONTACT_MATERIAL

    @staticmethod
    @overload
    def get_instance(width: int, height: int, name: str) -> str:
        return f"{Floor.ID} {'{'}\n" \
               f"{Floor.NAME} \"{name}\" \n" \
               f"{Floor.CONTACT_MATERIAL} \"concrete\"" \
               f"{Floor.SIZE} {width} {height} \n"


class Transform(features.Basic3DFeatures):
    ID: str = "Transform"
    SCALE: str = features.Features.SCALE
    ROTATION_STEP: str = features.Features.ROTATION_STEP
    CHILDREN: str = features.Features.CHILDREN


class Panel(features.Basic3DFeatures, Object3D):
    ID: str = "Panel"
    SIZE: str = features.Features.SIZE
    PANELS_COUNT: str = features.Features.PANELS_COUNT

    @staticmethod
    @overload
    def get_instance(name: str, rotation: np.array, translation: np.array, size: np.array, panel_count: int) -> str:
        return f"{Panel.ID} {'{'}\n" \
               f"{Panel.NAME} \"{name}\" \n" \
               f"{Panel.ROTATION} {rotation} \n" \
               f"{Panel.TRANSLATION} {translation} \n" \
               f"{Panel.SIZE} {size} \n" \
               f"{Panel.PANELS_COUNT} {panel_count} \n" \
               "}\n"


class WashingMachine(features.Basic3DFeatures, Object3D):
    ID: str = "WashingMachine"

    @staticmethod
    @overload
    def get_instance(name: str, rotation: np.array, translation: np.array) -> str:
        return f"{WashingMachine.ID} {'{'}\n" \
               f"{WashingMachine.NAME} \"{name}\" \n" \
               f"{WashingMachine.ROTATION} {rotation} \n" \
               f"{WashingMachine.TRANSLATION} {translation} \n" \
               "}\n"


class Bed(features.Basic3DFeatures):
    ID: str = "Bed"
    NAME: str = features.Features.NAME

    @staticmethod
    def get_instance(name: str, rotation: np.array, translation: np.array) -> str:
        return f"{Bed.ID} {'{'}\n" \
               f"{Bed.NAME} \"{name}\" \n" \
               f"{Bed.ROTATION} {rotation} \n" \
               f"{Bed.TRANSLATION} {translation} \n" \
               "}\n"


class Desk(features.Basic3DFeatures):
    ID: str = "Desk"
    NAME: str = features.Features.NAME

    @staticmethod
    def get_instance(name: str, rotation: np.array, translation: np.array) -> str:
        return f"{Desk.ID} {'{'}\n" \
               f"{Desk.NAME} \"{name}\" \n" \
               f"{Desk.ROTATION} {rotation} \n" \
               f"{Desk.TRANSLATION} {translation} \n" \
               "}\n"


class Fridge(features.Basic3DFeatures):
    ID: str = "Fridge"
    NAME: str = features.Features.NAME
    HIDDEN_POSITION: str = features.Features.HIDDEN_POSITION
    HIDDEN_ROTATION: str = features.Features.HIDDEN_ROTATION

    @staticmethod
    def get_instance(name: str, rotation: np.array, translation: np.array, hidden_rotation: np.array,
                     hidden_translation: np.array, index: int) -> str:
        return f"{Fridge.ID} {'{'}\n" \
               f"{Fridge.NAME} \"{name}\" \n" \
               f"{Fridge.ROTATION} {rotation} \n" \
               f"{Fridge.TRANSLATION} {translation} \n" \
               f"{Fridge.HIDDEN_ROTATION}_{index} {hidden_rotation} \n" \
               f"{Fridge.HIDDEN_POSITION}_{index} {hidden_translation} \n" \
               "}\n"


class Wall(features.Basic3DFeatures):
    ID: str = "Wall"
    NAME: str = features.Features.NAME
    SIZE: str = features.Features.SIZE
    APPEARANCE: str = features.Features.APPEARANCE

    @staticmethod
    def get_instance(name: str, translation: np.array, rotation: np.array, size: np.array) -> str:
        return f"{Wall.ID} {'{'}\n" \
               f"{Wall.NAME} \"wall\" \n" \
               f"{Wall.TRANSLATION} \n" \
               f"{Wall.ROTATION} \n" \
               f"{Wall.SIZE} \n" \
               f"{Wall.APPEARANCE} \n" \
               "}\n"


class Door:  # -> Daha sonra Eklenebilir. Simdilik gerek yok.
    pass


class Radiator(features.Basic3DFeatures):
    ID: str = "Radiator"
    NAME: str = features.Features.NAME
