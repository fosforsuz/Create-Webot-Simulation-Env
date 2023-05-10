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
    NUMBEROFFINS: str = "\tnumberOfFins"
    COLOR: str = "\tcolor"
    TEXTURE_URL: str = "\ttextureUrl"
    DISPLAY_WIDTH: str = "\tdisplayWidth"
    DISPLAY_HEIGHT: str = "\tdisplayHeight"
    STEP_SIZE: str = "\tstepSize"
    STEP_RISE: str = "\tstepRise"
    UPPER_APPEREANCE: str = "\tupperApperance"
    BOTTOM_APPEREANCE: str = "\tbottomApperance"
    DEPTH: str = "\tdepth"
    INNER_THICKNESS: str = "\tinnerThickness"
    OUTER_THICKNESS: str = "\touterThickness"


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


class GroundBase:
    CONTACT_MATERIAL: str = Features.CONTACT_MATERIAL
    FLOOR_SIZE: str = Features.FLOOR_SIZE
    

class HiddenFeatures:
    HIDDEN_POSITION: str = Features.HIDDEN_POSITION
    HIDDEN_ROTATION: str = Features.HIDDEN_ROTATION
    

class AppearanceFeatures:
    SIZE: str = Features.SIZE
    APPEARANCE: str = Features.APPEARANCE
    

class Display:
    COLOR: str = Features.COLOR
    TEXTURE_URL: str = Features.TEXTURE_URL


class DisplayDevice:
    DISPLAY_WIDTH: str = Features.DISPLAY_WIDTH
    DISPLAY_HEIGHT: str = Features.DISPLAY_HEIGHT


class StepInfo:
    STEP_SIZE: str = Features.STEP_SIZE
    STEP_RISE: str = Features.STEP_RISE


class Apperance:
    UPPER_APPEREANCE: str = "upperApperance"
    BOTTOM_APPEREANCE: str = "bottomApperance"


class ShapeProperties:
    DEPTH: str = Features.DEPTH
    INNER_THICKNESS: str = Features.INNER_THICKNESS
    OUTHER_THICKNESS: str = Features.OUTER_THICKNESS