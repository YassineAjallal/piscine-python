from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        super().__init__(first_name, is_alive)

    def get_eyes(self) -> str:
        return (self.eyes)

    def get_hairs(self) -> str:
        return (self.hairs)

    def set_eyes(self, eyes: str) -> None:
        self.eyes = eyes

    def set_hairs(self, hairs: str) -> None:
        self.hairs = hairs
