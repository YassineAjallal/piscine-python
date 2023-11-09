from abc import ABC, abstractmethod


class Character(ABC):
    """Character class doc"""
    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Constructor Character doc"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        "Character die doc"
        pass


class Stark(Character):
    """Stark class doc"""
    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Stark Character doc"""
        super().__init__(first_name, is_alive)

    def die(self):
        "Stark die doc"
        self.is_alive = False
