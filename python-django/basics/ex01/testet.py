from intern import Intern


if __name__ == "__main__":
    inter1 = Intern()
    inter2 = Intern("Mark")

    print(inter1.name)
    print(inter2.name)

    print(inter1.make_coffee())

    try:
        inter2.work()
    except Exception as a:
        print(a)
