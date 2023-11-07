
global Nothing
global Garlic
global Zero
global Empty
global Fake

def NULL_not_found(object: any) -> int:
    names = {"Nothing" : None, "Garlic" : float("NaN"), "Zero" : 0, "Empty" : "", "Fake" : False}
    for name in names :
        if ((not object) or object != object) and (type(names[name]) == type(object)):
            print(f"{name}: {object} {type(object)}")
            return (0)
    print("Type not Found")
    return (1)
