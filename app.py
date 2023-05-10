from models.world import World
from lib.utility import create_folder_structure
from typing import Tuple
from create_env import CreateEnv
import customtkinter
import string


class SimulationApp(customtkinter.CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)

        self.title("Dunya Yaratici")
        self.geometry("450x450")

        # Create Header Label
        self.header_label = customtkinter.CTkLabel(
            master=self, text="Dünya Yaratıcı", font=("Arial", 30), corner_radius=8)
        self.header_label.place(relx=0.5, rely=0.1, anchor="center")

        # Create World Name Label
        self.world_name_label = customtkinter.CTkLabel(
            master=self, text="Klasör Adı", font=("Arial", 20), corner_radius=8)
        self.world_name_label.place(relx=0.35, rely=0.3, anchor="center")

        # Create World Name Entry
        self.world_name_entry = customtkinter.CTkEntry(
            master=self, font=("Arial", 20), corner_radius=8)
        self.world_name_entry.place(relx=0.65, rely=0.3, anchor="center")

        # Create World Width Label
        self.width_label = customtkinter.CTkLabel(
            master=self, text="Genişlik", font=("Arial", 20), corner_radius=8)
        self.width_label.place(relx=0.35, rely=0.4, anchor="center")

        # Create World Width Entry
        self.width_entry = customtkinter.CTkEntry(
            master=self, font=("Arial", 20), corner_radius=8)
        self.width_entry.place(relx=0.65, rely=0.4, anchor="center")

        # Create World Length Label
        self.length_label = customtkinter.CTkLabel(
            master=self, text="Uzunluk", font=("Arial", 20), corner_radius=8)
        self.length_label.place(relx=0.35, rely=0.5, anchor="center")

        # Create World Length Entry
        self.length_entry = customtkinter.CTkEntry(
            master=self, font=("Arial", 20), corner_radius=8)
        self.length_entry.place(relx=0.65, rely=0.5, anchor="center")

        # Create Number of Floors Label
        self.number_of_floors_label = customtkinter.CTkLabel(
            master=self, text="Kat Sayısı", font=("Arial", 20), corner_radius=8)
        self.number_of_floors_label.place(relx=0.35, rely=0.6, anchor="center")

        # Create Number of Floors Entry
        self.number_of_floors_entry = customtkinter.CTkEntry(
            master=self, font=("Arial", 20), corner_radius=8)
        self.number_of_floors_entry.place(relx=0.65, rely=0.6, anchor="center")

        # Create Button
        self.button = customtkinter.CTkButton(master=self, text="Oluştur", font=(
            "Arial", 20), corner_radius=8, command=self.button_handler)
        self.button.place(relx=0.5, rely=0.8, anchor="center")

    def button_handler(self):
        if self.world_name_entry.get() == "" or self.width_entry.get() == "" or self.length_entry.get() == "" or self.number_of_floors_entry.get() == "":
            self.error_message = customtkinter.CTkLabel(
                master=self, text="Lütfen tüm alanları doldurunuz.", font=("Arial", 20), corner_radius=8, bg_color="red")
            self.error_message.place(relx=0.5, rely=0.9, anchor="center")

        else:
            if "error_message" in self.__dict__.keys():
                self.error_message.destroy()
            self.check_variables()

    def check_variables(self):
        control: bool = False
        if self.is_valid_directory_name():
            control = True

        if not self.is_alpha(self.width_entry.get()):
            control = True

        if not self.is_alpha(self.length_entry.get()):
            control = True

        if not self.is_alpha(self.number_of_floors_entry.get()):
            control = True

        if control:
            self.error_message = customtkinter.CTkLabel(
                master=self, text="Lütfen geçerli değerler giriniz.", font=("Arial", 20), corner_radius=8, bg_color="red")
            self.error_message.place(relx=0.5, rely=0.9, anchor="center")
        else:
            self.create_simulation()

    def is_valid_directory_name(self) -> bool:
        for char in self.world_name_entry.get():
            if char in string.punctuation:
                return True
        return False

    def is_alpha(self, number: str) -> bool:
        for num in number:
            if num.isalpha():
                return False
        return True
    
    def create_variables(self) -> None:
        self.create_world_variable()
        self.create_env_variables()
    
    def create_world_variable(self) -> None:
        self.world = World()
        self.world.name = self.world_name_entry.get()
        self.world.width = int(self.width_entry.get())
        self.world.length = int(self.length_entry.get())
        self.world.count = int(self.number_of_floors_entry.get())
        self.world.world_file_path = create_folder_structure(self.world.name)
        
    def create_env_variables(self) -> None:
        self.env = CreateEnv(world=self.world)
    
    def create_simulation(self) -> None:
        self.create_variables()
        self.env.create_scene_settings()
        self.env.create_materials()
    

if __name__ == "__main__":
    app = SimulationApp()
    app.mainloop()
