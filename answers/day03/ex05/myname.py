class monster:
    def __init__(self) -> None:
        self.name = "Slime"

    @property
    def myname(self) -> str:
        return self.name

    @myname.setter
    def myname(self, name : str) -> None:
        self.name = name