import lib.features_parents as Features
from lib.object3D import Object3D
from lib.abstract import Instance


class PhotoFrame(Features.Basic3DFeatures, Instance):
    ID: str = "PhotoFrame"

    @staticmethod
    def get_instance(object_count: int) -> str:
        return PhotoFrame.ID \
            + Object3D.OPEN_SECTION \
            + Object3D.return_name(id=PhotoFrame.ID, object_count=object_count) \
            + Object3D.return_translation(physics=True) \
            + Object3D.return_rotation(physics=True) \
            + Object3D.return_physics() \
            + Object3D.CLOSE_SECTION


class Chair(Features.Basic3DFeatures, Instance):
    ID: str = "Chair"

    @staticmethod
    def get_instance(object_count: int) -> str:
        return Chair.ID \
            + Object3D.OPEN_SECTION \
            + Object3D.return_translation(physics=True) \
            + Object3D.return_rotation(physics=True) \
            + Object3D.return_name(id=Chair.ID, object_count=object_count) \
            + Object3D.return_physics() \
            + Object3D.CLOSE_SECTION


class OfficeChair(Features.Basic3DFeatures, Instance):
    ID: str = "OfficeChair"

    @staticmethod
    def get_instance(object_count: int) -> str:
        return OfficeChair.ID \
            + Object3D.OPEN_SECTION \
            + Object3D.return_translation(physics=True) \
            + Object3D.return_rotation(physics=True) \
            + Object3D.return_name(object_count=object_count, id=OfficeChair.ID) \
            + Object3D.return_enable_physics() \
            + Object3D.CLOSE_SECTION


class WoodenChair(Features.Basic3DFeatures, Instance):
    ID: str = "WoodenChair"

    @staticmethod
    def get_instance(object_count: int) -> str:
        return WoodenChair.ID \
            + Object3D.OPEN_SECTION \
            + Object3D.return_translation(physics=True) \
            + Object3D.return_rotation(physics=True) \
            + Object3D.return_name(object_count=object_count, id=WoodenChair.ID) \
            + Object3D.return_physics() \
            + Object3D.CLOSE_SECTION


class Barbecue(Features.Basic3DFeatures, Instance):
    ID: str = "Barbecue"

    @staticmethod
    def get_instance(object_count: int) -> str:
        return Barbecue.ID \
            + Object3D.OPEN_SECTION \
            + Object3D.return_translation(physics=True) \
            + Object3D.return_rotation(physics=True) \
            + Object3D.return_name(object_count=object_count, id=Barbecue.ID) \
            + Object3D.return_enable_physics() \
            + Object3D.CLOSE_SECTION


class Gnome(Features.Basic3DFeatures, Instance):
    ID: str = "Gnome"

    @staticmethod
    def get_instance(object_count: int) -> str:
        return Gnome.ID \
            + Object3D.OPEN_SECTION \
            + Object3D.return_translation(physics=True) \
            + Object3D.return_rotation(physics=True) \
            + Object3D.return_name(object_count=object_count, id=Gnome.ID) \
            + Object3D.return_enable_physics() \
            + Object3D.CLOSE_SECTION


class WateringCan(Features.Basic3DFeatures, Instance):
    ID: str = "WateringCan"

    @staticmethod
    def get_instance(object_count: int) -> str:
        return WateringCan.ID \
            + Object3D.OPEN_SECTION \
            + Object3D.return_translation(physics=True) \
            + Object3D.return_rotation(physics=True) \
            + Object3D.return_name(object_count=object_count, id=WateringCan.ID) \
            + Object3D.return_enable_physics() \
            + Object3D.CLOSE_SECTION


class Wheelbarrow(Features.Basic3DFeatures, Instance):
    ID: str = "Wheelbarrow"

    @staticmethod
    def get_instance(object_count: int) -> str:
        return Wheelbarrow.ID \
            + Object3D.OPEN_SECTION \
            + Object3D.return_translation(physics=True) \
            + Object3D.return_rotation(physics=True) \
            + Object3D.return_name(object_count=object_count, id=Wheelbarrow.ID) \
            + Object3D.return_enable_physics() \
            + Object3D.CLOSE_SECTION


class MedicineBottle(Features.Basic3DFeatures, Instance):
    ID: str = "MedicineBottle"

    @staticmethod
    def get_instance(object_count: int) -> str:
        return MedicineBottle.ID \
            + Object3D.OPEN_SECTION \
            + Object3D.return_translation(physics=True) \
            + Object3D.return_rotation(physics=True) \
            + Object3D.return_name(object_count=object_count, id=MedicineBottle.ID) \
            + Object3D.return_physics() \
            + Object3D.CLOSE_SECTION


class Floorlight(Features.Basic3DFeatures, Instance):
    ID: str = "FloorLight"

    @staticmethod
    def get_instance(object_count: int) -> str:
        return Floorlight.ID \
            + Object3D.OPEN_SECTION \
            + Object3D.return_translation(physics=True) \
            + Object3D.return_rotation(physics=True) \
            + Object3D.return_name(object_count=object_count, id=Floorlight.ID) \
            + Object3D.return_physics() \
            + Object3D.CLOSE_SECTION


class Sofa(Features.Basic3DFeatures, Instance):
    ID: str = "Sofa"

    @staticmethod
    def get_instance(object_count: int) -> str:
        return Sofa.ID \
            + Object3D.OPEN_SECTION \
            + Object3D.return_translation(physics=True) \
            + Object3D.return_rotation(physics=True) \
            + Object3D.return_name(object_count=object_count, id=Sofa.ID) \
            + Object3D.return_physics() \
            + Object3D.CLOSE_SECTION


class Armchair(Features.Basic3DFeatures, Instance):
    ID: str = "Armchair"

    @staticmethod
    def get_instance(object_count: int) -> str:
        return Sofa.ID \
            + Object3D.OPEN_SECTION \
            + Object3D.return_translation(physics=True) \
            + Object3D.return_rotation(physics=True) \
            + Object3D.return_name(object_count=object_count, id=Armchair.ID) \
            + Object3D.return_physics() \
            + Object3D.CLOSE_SECTION


class Mirror(Features.Basic3DFeatures, Instance):
    ID: str = "Mirror"

    @staticmethod
    def get_instance(object_count: int) -> str:
        return Mirror.ID \
            + Object3D.OPEN_SECTION \
            + Object3D.return_translation(physics=True) \
            + Object3D.return_rotation(physics=True) \
            + Object3D.return_name(object_count=object_count, id=Mirror.ID) \
            + Object3D.return_physics() \
            + Object3D.CLOSE_SECTION


class BunchOfSunFlowers(Features.Basic3DFeatures, Instance):
    ID: str = "BunchOfSunFlowers"

    @staticmethod
    def get_instance(object_count: int) -> str:
        return BunchOfSunFlowers.ID \
            + Object3D.OPEN_SECTION \
            + Object3D.return_translation(physics=True) \
            + Object3D.return_rotation(physics=True) \
            + Object3D.return_name(object_count=object_count, id=BunchOfSunFlowers.ID) \
            + Object3D.return_physics() \
            + Object3D.CLOSE_SECTION


class FlowerPot(Features.Basic3DFeatures, Instance):
    ID: str = "FlowerPot"

    @staticmethod
    def get_instance(object_count: int) -> str:
        return FlowerPot.ID \
            + Object3D.OPEN_SECTION \
            + Object3D.return_translation(physics=True) \
            + Object3D.return_rotation(physics=True) \
            + Object3D.return_name(object_count=object_count, id=FlowerPot.ID) \
            + Object3D.return_physics() \
            + Object3D.CLOSE_SECTION


class Desk(Features.Basic3DFeatures, Instance):
    ID: str = "Desk"

    @staticmethod
    def get_instance(object_count: int) -> str:
        return Desk.ID \
            + Object3D.OPEN_SECTION \
            + Object3D.return_translation(physics=True) \
            + Object3D.return_rotation(physics=True) \
            + Object3D.return_name(object_count=object_count, id=Desk.ID) \
            + Object3D.return_physics() \
            + Object3D.CLOSE_SECTION


class PottedTree(Features.Basic3DFeatures, Instance):
    ID: str = "PottedTree"

    @staticmethod
    def get_instance(object_count: int) -> str:
        return PottedTree.ID \
            + Object3D.OPEN_SECTION \
            + Object3D.return_translation(physics=True) \
            + Object3D.return_rotation(physics=True) \
            + Object3D.return_name(object_count=object_count, id=PottedTree.ID) \
            + Object3D.return_physics() \
            + Object3D.CLOSE_SECTION


class RoundTable(Features.Basic3DFeatures, Instance):
    ID: str = "RoundTable"

    @staticmethod
    def get_instance(object_count: int) -> str:
        return RoundTable.ID \
            + Object3D.OPEN_SECTION \
            + Object3D.return_translation(physics=True) \
            + Object3D.return_rotation(physics=True) \
            + Object3D.return_name(object_count=object_count, id=RoundTable.ID) \
            + Object3D.return_physics() \
            + Object3D.CLOSE_SECTION


class OfficeTelephone(Features.Basic3DFeatures, Instance):
    ID: str = "OfficeTelephone"

    @staticmethod
    def get_instance(object_count: int) -> str:
        return OfficeTelephone.ID \
            + Object3D.OPEN_SECTION \
            + Object3D.return_translation(physics=True) \
            + Object3D.return_rotation(physics=True) \
            + Object3D.return_name(object_count=object_count, id=OfficeTelephone.ID) \
            + Object3D.return_enable_physics() \
            + Object3D.CLOSE_SECTION
