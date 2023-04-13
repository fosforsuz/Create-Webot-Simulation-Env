class World:
    name: str
    width: int
    length: int
    count: int
    world_file_path: str
    space: str = ' '*8

    def __str__(self):
        return f"\nName: {self.name}\n{self.space}└──Width: {self.width}\n{self.space}└──Length: {self.length}\n{self.space}└──Count: {self.count}"
