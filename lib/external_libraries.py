token: str = "#VRML_SIM R2023a utf8\n"

libraries: str = '''EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/traffic/protos/CrossRoadsTrafficLight.proto"
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/apartment_structure/protos/Wall.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/bedroom/protos/Bed.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/trees/protos/Oak.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/buildings/protos/FastFoodRestaurant.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/chairs/protos/Chair.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/traffic/protos/StopSign.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/appearances/protos/Roughcast.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/tables/protos/Desk.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/traffic/protos/GenericTrafficLight.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/buildings/protos/ResidentialBuilding.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/road/protos/StraightRoadSegment.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/trees/protos/BigSassafras.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/trees/protos/Pine.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/road/protos/CurvedRoadSegment.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/road/protos/RoadLine.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/buildings/protos/BuildingUnderConstruction.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/traffic/protos/SpeedLimitPanel.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/buildings/protos/Museum.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/kitchen/oven/protos/Oven.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/traffic/protos/TrafficCone.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/traffic/protos/CautionPanel.proto"
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/buildings/protos/TheThreeTowers.proto"
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/panels/protos/Panel.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/buildings/protos/BigGlassTower.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/trees/protos/Sassafras.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/apartment_structure/protos/Radiator.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/buildings/protos/CyberboticsTower.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/buildings/protos/HollowBuilding.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/traffic/protos/YieldSign.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/traffic/protos/SpeedLimitSign.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/traffic/protos/OrderSign.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/buildings/protos/Auditorium.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/backgrounds/protos/TexturedBackgroundLight.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/bathroom/protos/Bathtube.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/bathroom/protos/WashingMachine.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/trees/protos/Cypress.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/traffic/protos/HighwayPole.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/traffic/protos/HighwaySign.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/kitchen/fridge/protos/Fridge.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/obstacles/protos/OilBarrel.proto"
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/traffic/protos/StopPanel.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/floors/protos/Floor.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/cabinet/protos/Cabinet.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/living_room_furniture/protos/Armchair.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/bathroom/protos/Toilet.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/devices/sick/protos/SickLms291.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/buildings/protos/UBuilding.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/buildings/protos/Hotel.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/road/protos/RoadIntersection.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/traffic/protos/CautionSign.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/backgrounds/protos/TexturedBackground.proto"
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/traffic/protos/OrderPanel.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/traffic/protos/PedestrianCrossing.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/advertising_board/protos/AdvertisingBoard.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/buildings/protos/CommercialBuilding.proto"
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/living_room_furniture/protos/Sofa.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/floors/protos/RectangleArena.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/vehicles/protos/bmw/BmwX5.proto" 
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/road/protos/Crossroad.proto"
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/appearances/protos/Parquetry.proto"
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/school_furniture/protos/Clock.proto"
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/television/protos/Television.proto"
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/bathroom/protos/BathroomSink.proto"
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/school_furniture/protos/Book.proto"
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/paintings/protos/LandscapePainting.proto"
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/objects/apartment_structure/protos/Ceiling.proto"
'''

create_ground: str = '''
DEF GROUND Solid {
    translation 0 0 -0.1
    rotation 0 0 1 0
    children [
        Shape {
            appearance PBRAppearance {
                baseColor 0.8 0.8 0.8
                baseColorMap ImageTexture {
                url [
                    "https://raw.githubusercontent.com/cyberbotics/webots/R2023a/projects/vehicles/worlds/textures/ground.jpg"
                ]
            }
            roughness 0.5
            metalness 0
            textureTransform TextureTransform {
                scale 500 500
            }
        }
        geometry DEF GROUND_PLANE Plane {
            size 2000 2000
            }
        }
    ]
}
'''
