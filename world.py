class World:
    name: str
    width: int
    length: int
    count: int
    world_file_path: str
    space: str = " " * 8

    def __str__(self) -> str:
        return (
            f"\nName: {self.name}\n"
            + f"{self.space}└──Width: {self.width}\n{self.space}└──Length: {self.length}\n{self.space}└──Count: {self.count}\n{self.space}└──File Path: {self.world_file_path}\n"
        )
