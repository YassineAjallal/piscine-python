class HotBeverage:
    def __init__(self, name: str = "hot beverage", price: float = 0.30,
                 description: str = "Just some hot water in a cup.") -> None:
        self._price = price
        self._name = name
        self._description = description

    def description(self) -> str:
        return (self._description)

    def __str__(self) -> str:
        return (f"""name : {self._name}
price : {self._price}
description : {self.description()}
""")


class Coffee(HotBeverage):
    def __init__(self) -> None:
        super().__init__("coffee", 0.40, "A coffee, to stay awake.")


class Tea(HotBeverage):
    def __init__(self) -> None:
        super().__init__("tea")


class Chocolate(HotBeverage):
    def __init__(self) -> None:
        super().__init__("chocolate", 0.50, "Chocolate, sweet chocolate...")


class Cappuccino(HotBeverage):
    def __init__(self) -> None:
        super().__init__("cappuccino", 0.45,
                         "Un po' di Italia nella sua tazza!")
