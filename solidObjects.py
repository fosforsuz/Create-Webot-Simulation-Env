import numpy as np


class Features:
    NAME: str = "\tname"
    APPEARANCE: str = "\tappearance"
    COORDINATE_SYSTEM: str = "\tcoordinateSystem \"NUE\"\n"
    TRANSLATION: str = "\ttranslation"
    ORIENTATION: str = "\torientation"
    ROTATION: str = "\trotation"
    POSITION: str = "\tposition"
    TEXTURE: str = "\ttexture"
    LUMINOSITY: str = "\tluminosity"
    SCALE: str = "\tscale"
    SIZE: str = "\tsize"
    TILE_SIZE: str = "\ttileSize"
    SKYBOX: str = "\tskybox"
    CASTSHADOWS: str = "\tcastShadows"
    CONTACT_MATERIAL: str = "\tcontactMaterial"
    FLOOR_SIZE: str = "\tfloorSize"
    ROTATION_STEP: str = "\trotationStep"
    CHILDREN: str = "\tchildren"
    PANELS_COUNT: str = "\tpanelsCount"
    HIDDEN_POSITION: str = "\thidden position_0"
    HIDDEN_ROTATION: str = "\thidden rotation_"


class Transformation:
    TRANSLATION: str = Features.TRANSLATION
    ROTATION: str = Features.ROTATION


class WorldInfo:
    ID: str = "WorldInfo"
    COORDINATE_SYSTEM: str = Features.COORDINATE_SYSTEM

    @staticmethod
    def get_instance() -> str:
        return WorldInfo.ID + "{\n" \
            + WorldInfo.COORDINATE_SYSTEM \
            + "}\n"


class ViewPoint:
    ID: str = "Viewpoint"
    ORIENTATION: str = Features.ORIENTATION
    POSITION: str = Features.POSITION

    @staticmethod
    def get_instance() -> str:
        return f"{ViewPoint.ID} {'{'}\n" \
               f"{ViewPoint.ORIENTATION} 0.06055435408039591 -0.033257383193768815 -0.9976107039647324 " \
               f"3.153653224698355 \n" \
               f'{ViewPoint.POSITION} 13.648152950347704 3.748782732166771 1.0662266522655417 \n' \
               "}\n"


class TexturedBackground:
    ID: str = "TexturedBackground"
    TEXTURE: str = Features.TEXTURE
    LUMINOSITY: str = Features.LUMINOSITY
    SKYBOX: str = Features.SKYBOX

    @staticmethod
    def get_instance() -> str:
        return f"{TexturedBackground.ID} {'{'} {'}'}\n"


class TexturedBackgroundLight:
    ID: str = "TexturedBackgroundLight"
    TEXTURE: str = Features.TEXTURE
    LUMINOSITY: str = Features.LUMINOSITY
    CAST_SHADOWS: str = Features.CASTSHADOWS

    @staticmethod
    def get_instance() -> str:
        return f"{TexturedBackgroundLight.ID} {'{'} {'}'}\n"


class RectangleArena(Transformation):
    ID: str = "RectangleArena"
    NAME: str = Features.NAME
    CONTACT_MATERIAL: str = Features.CONTACT_MATERIAL
    FLOOR_SIZE: str = Features.FLOOR_SIZE

    @staticmethod
    def get_instance(width: int, height: int, name: str) -> str:
        return f"{RectangleArena.ID} {'{'}\n" \
               f"{RectangleArena.NAME} \"{name}\" \n" \
               f"{RectangleArena.CONTACT_MATERIAL} \"concrete\" \n" \
               f"{RectangleArena.FLOOR_SIZE} {width} {height} \n" \
               "}\n"


class Floor(Transformation):
    ID: str = "Floor"
    NAME: str = Features.NAME
    SIZE: str = Features.SIZE
    TILE_SIZE: str = Features.TILE_SIZE
    CONTACT_MATERIAL: str = Features.CONTACT_MATERIAL

    @staticmethod
    def get_instance(width: int, height: int, name: str) -> str:
        return f"{Floor.ID} {'{'}\n" \
               f"{Floor.NAME} \"{name}\" \n" \
               f"{Floor.CONTACT_MATERIAL} \"concrete\"" \
               f"{Floor.SIZE} {width} {height} \n"


class Transform(Transformation):
    ID: str = "Transform"
    SCALE: str = Features.SCALE
    ROTATION_STEP: str = Features.ROTATION_STEP
    CHILDREN: str = Features.CHILDREN


class Panel(Transformation):
    ID: str = "Panel"
    NAME: str = Features.NAME
    SIZE: str = Features.SIZE
    PANELS_COUNT: str = Features.PANELS_COUNT

    @staticmethod
    def get_instance(name: str, rotation: np.array, translation: np.array, size: np.array, panel_count: int) -> str:
        return f"{Panel.ID} {'{'}\n" \
               f"{Panel.NAME} \"{name}\" \n" \
               f"{Panel.ROTATION} {rotation} \n" \
               f"{Panel.TRANSLATION} {translation} \n" \
               f"{Panel.SIZE} {size} \n" \
               f"{Panel.PANELS_COUNT} {panel_count} \n" \
               "}\n"


class WashingMachine(Transformation):
    ID: str = "WashingMachine"
    NAME: str = Features.NAME

    @staticmethod
    def get_instance(name: str, rotation: np.array, translation: np.array) -> str:
        return f"{WashingMachine.ID} {'{'}\n" \
               f"{WashingMachine.NAME} \"{name}\" \n" \
               f"{WashingMachine.ROTATION} {rotation} \n" \
               f"{WashingMachine.TRANSLATION} {translation} \n" \
               "}\n"


class Bed(Transformation):
    ID: str = "Bed"
    NAME: str = Features.NAME

    @staticmethod
    def get_instance(name: str, rotation: np.array, translation: np.array) -> str:
        return f"{Bed.ID} {'{'}\n" \
               f"{Bed.NAME} \"{name}\" \n" \
               f"{Bed.ROTATION} {rotation} \n" \
               f"{Bed.TRANSLATION} {translation} \n" \
               "}\n"


class Desk(Transformation):
    ID: str = "Desk"
    NAME: str = Features.NAME

    @staticmethod
    def get_instance(name: str, rotation: np.array, translation: np.array) -> str:
        return f"{Desk.ID} {'{'}\n" \
               f"{Desk.NAME} \"{name}\" \n" \
               f"{Desk.ROTATION} {rotation} \n" \
               f"{Desk.TRANSLATION} {translation} \n" \
               "}\n"


class Fridge(Transformation):
    ID: str = "Fridge"
    NAME: str = Features.NAME
    HIDDEN_POSITION: str = Features.HIDDEN_POSITION
    HIDDEN_ROTATION: str = Features.HIDDEN_ROTATION

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


class Wall:
    ID: str = "Wall"


class MainElements:
    WORLD_INFO = WorldInfo
    VIEW_POINT = ViewPoint
    TEXTURED_BACKGROUND = TexturedBackground
    TEXTURED_BACKGROUND_LIGHT = TexturedBackgroundLight
    RECTANGLE_ARENA = RectangleArena
    FLOOR = Floor
    TRANSFORM = Transform
    PANEL = Panel
    BED = Bed
    DESK = Desk
    FRIDGE = Fridge
    WALL = Wall
