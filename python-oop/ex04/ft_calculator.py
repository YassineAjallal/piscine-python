class calculator:
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        lst: list[float] = []
        for i in range(len(V1)):
            lst.append(V1[i] * V2[i])
        print("Dot product is:", sum(lst))

    def add_vec(V1: list[float], V2: list[float]) -> None:
        lst: list[float] = []
        for i in range(len(V1)):
            lst.append(float(V1[i] + V2[i]))
        print("Add Vector is:", lst)

    def sous_vec(V1: list[float], V2: list[float]) -> None:
        lst: list[float] = []
        for i in range(len(V1)):
            lst.append(float(V1[i] - V2[i]))
        print("Sous Vector is :", lst)
