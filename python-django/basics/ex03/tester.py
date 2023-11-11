from machine import CoffeeMachine
from beverages import HotBeverage, Tea, Cappuccino, Chocolate, Coffee


if __name__ == "__main__":
    coffee = CoffeeMachine()
    print(coffee.serve(HotBeverage))
    print(coffee.serve(Tea))
    print(coffee.serve(Cappuccino))
    print(coffee.serve(Chocolate))
    print(coffee.serve(Coffee))

    print(coffee.serve(HotBeverage))
    print(coffee.serve(Tea))
    print(coffee.serve(Cappuccino))
    print(coffee.serve(Chocolate))
    print(coffee.serve(Coffee))
    try:
        print(coffee.serve(Coffee))
    except Exception as err:
        print(err)
    coffee.repair()
    print(coffee.serve(Coffee))
