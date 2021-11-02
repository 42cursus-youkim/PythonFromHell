class monster:
    def __init__(self, name : str) -> None:
        self.name: str = name

    def say_myname(self) -> None:
        print(self.name)