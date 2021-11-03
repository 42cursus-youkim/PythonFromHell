class monster:
    def __init__(self, name: str, hp: int, level: int, exp: int) -> None:
        self.name = name
        self.hp = hp
        self.level = level
        self.exp = exp

    def change_level(self, level) -> None:
        dif_level: int = level - self.level
        self.level = level
        self.hp += dif_level * 10
        if self.hp < 10:
            self.hp = 10
        self.exp += dif_level * 10
        if self.exp < 10:
            self.exp = 10