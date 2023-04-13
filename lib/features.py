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


class Basic3DFeatures:
    NAME: str = Features.NAME
    TRANSLATION: str = Features.TRANSLATION
    ROTATION: str = Features.ROTATION


class Positional3DFeatures:
    POSITION: str = Features.POSITION
    ORIENTATION: str = Features.ORIENTATION


class TextureBase:
    TEXTURE: str = Features.TEXTURE
    LUMINOSITY: str = Features.LUMINOSITY
    SKYBOX: str = Features.SKYBOX
    CAST_SHADOWS: str = Features.CASTSHADOWS
