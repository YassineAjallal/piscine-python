class calculator:
    def __init__(self, lst: list) -> None:
        self.numbers_list = lst

    def __add__(self, object) -> None:
        self.numbers_list = [nb + object for nb in self.numbers_list]
        print(self.numbers_list)

    def __mul__(self, object) -> None:
        self.numbers_list = [nb * object for nb in self.numbers_list]
        print(self.numbers_list)

    def __sub__(self, object) -> None:
        self.numbers_list = [nb - object for nb in self.numbers_list]
        print(self.numbers_list)

    def __truediv__(self, object) -> None:
        if (object != 0):
            self.numbers_list = [nb / object for nb in self.numbers_list]
            print(self.numbers_list)
        else:
            print("impossible the devise by zero")
