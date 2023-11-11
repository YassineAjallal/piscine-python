from beverages import HotBeverage
import random


class CoffeeMachine:
    def __init__(self) -> None:
        self.nb_drinks = 0

    class EmptyCup(HotBeverage):
        def __init__(self) -> None:
            super().__init__("empty cup", 0.90,
                             "An empty cup?! Gimme my money back!")

    class BrokenMachineException(Exception):
        def __init__(self) -> None:
            super().__init__("This coffee machine has to be repaired.")

    def repair(self) -> None:
        self.nb_drinks = 0

    def serve(self, beverage: HotBeverage):
        if self.nb_drinks < 10:
            self.nb_drinks += 1
            if (int(random.random() * 100) % 2 == 0):
                return (beverage())
            else:
                return (CoffeeMachine.EmptyCup())
        else:
            raise CoffeeMachine.BrokenMachineException()
