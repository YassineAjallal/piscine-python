class Intern:
    def __init__(self, name: str =
                 "My name? I'm nobody, an intern, I have no name.") -> None:
        self.name = name

    def __str__(self) -> str:
        return (self.name)

    class Coffee:
        def __str__(self) -> str:
            return ("This is the worst coffee you ever tasted.")

    def work(self) -> None:
        raise Exception("I'm just an intern, I can't do that...")

    def make_coffee(self) -> None:
        return self.Coffee()
