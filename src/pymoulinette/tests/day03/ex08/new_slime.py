from balance import monster

class slime(monster):
    def __init__(self, name: str, hp: int, level: int, exp: int) -> None:
        super().__init__(name, hp, level, exp)
        self._atk = 50
    
    @property
    def atk(self):
        return self.__atk
    
    @atk.setter
    def atk(self, atk):
        if atk < 0:
            raise ValueError("atk error")
        self._atk = atk
    
    def change_level(self, level) -> None:
        dif_level: int = level - self.level
        super().change_level(level)
        new_atk = self.__atk + dif_level*5
        if new_atk < 0:
            raise ValueError("atk error")
        self.__atk = new_atk