import os
import lib.external_libraries as external_libraries
from lib.folderStructure import FolderStructure


def show_exists_info(folder_name: str):
    print("*" * len(folder_name))
    print(f"{folder_name} dosya mevcut. Lutfen farkli bir isim deneyin.")
    print("*" * len(folder_name))
    exit(1)


def create_folder_structure(folder_name: str):
    path: str = os.path.join(FolderStructure.CURRENT_DIRECTORY.value, folder_name)
    if os.path.exists(path=path):
        show_exists_info(path)

    os.mkdir(path=path)

    print()
    for folder_path in FolderStructure:

        if folder_path not in [FolderStructure.CURRENT_DIRECTORY]:
            print(f"{folder_path.value} klasörü oluşturuluyor...")
            os.mkdir(os.path.join(path, folder_path.value))

    print()

    prepare_template(os.path.join(path, FolderStructure.WORLDS_PATH.value), folder_name)
    return os.path.join(os.path.join(path, FolderStructure.WORLDS_PATH.value), f"{folder_name}.wbt")


def prepare_template(path: str, file_name: str):
    with open(f"{path}/{file_name}.wbt", 'a') as file:
        file.write(f"{external_libraries.token}\n")
        file.write(f"{external_libraries.libraries}\n")


def create_main_structure(path: str, template):
    with open(path, 'a') as file:
        file.write(f"{template}\n")
        
