class monster:
    def __init__(self) -> None:
        self.name : str = "Slime"

    def get_name(self) -> str:
        return self.name

    def set_name(self, name : str) -> None:
        self.name = name