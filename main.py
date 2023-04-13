from world import World
from create_env import CreateEnv
from utility import create_folder_structure
import argparse


def print_world_infoes(world: World) -> None:
    print(f"\n{world}\n")


if __name__ == "__main__":
    world = World()
    parser = argparse.ArgumentParser(description="Bu script ile rastgele bir webots dünyası oluşturabilirsiniz.")

    parser.add_argument("-n", "--name", help="Dünyanın adı", required=False, default="new_world")
    parser.add_argument("-w", "--width", help="Binanın genişliği", required=False, default=10)
    parser.add_argument("-l", "--length", help="Binanın uzunluğu", required=False, default=10)
    parser.add_argument("-c", "--count", help="Binanın içerisindeki kat sayısı", required=False, default=1)

    world.name = parser.parse_args().name
    world.width = parser.parse_args().width
    world.length = parser.parse_args().length
    world.count = parser.parse_args().count

    world.world_file_path = create_folder_structure(world.name)  # Burada dünyanın dosya yolunu alıyoruz.
    
    print_world_infoes(world)

    env = CreateEnv(world)
