import models.homeStuffs as HomeStuffs

class HomeStuff:
    PHOTO_FRAME = HomeStuffs.PhotoFrame
    CHAIR = HomeStuffs.Chair
    OFFICE_CHAIR = HomeStuffs.OfficeChair
    WOODEN_CHAIR = HomeStuffs.WoodenChair
    BARBECUE = HomeStuffs.Barbecue
    GNOME = HomeStuffs.Gnome
    WATERING_CAN = HomeStuffs.WateringCan
    WHEEL_BARROW = HomeStuffs.Wheelbarrow
    MEDICINE_BOTTLE = HomeStuffs.MedicineBottle
    FLOOR_LIGHT = HomeStuffs.Floorlight
    SOFA = HomeStuffs.Sofa
    ARM_CHAIR = HomeStuffs.Armchair
    MIRROR = HomeStuffs.Mirror
    BUNCH_OF_FLOWERS = HomeStuffs.BunchOfSunFlowers
    FLOWER_POT = HomeStuffs.FlowerPot
    DESK = HomeStuffs.Desk
    ROUND_TABLE = HomeStuffs.RoundTable
    OFFICE_TELEPHONE = HomeStuffs.OfficeTelephone
    POTTED_TREE = HomeStuffs.PottedTree
    
    @staticmethod
    def __iterate_key__():
        for key, val in HomeStuff.__dict__.items():
            if not key.startswith("__"):
                yield key
    
    
    @staticmethod
    def __iterate_val__():
        for key, val in HomeStuff.__dict__.items():
            if not key.startswith("__"):
                yield val
    
    
    @staticmethod
    def __iterate_key_val__():
        for key, val in HomeStuff.__dict__.items():
            if not key.startswith("__"):
                yield key, val