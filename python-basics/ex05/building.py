import sys


def ispunct(string: str) -> bool:
    "Return True if a string is a punctuation mark otherwise False"
    return (not (string.isupper() or string.islower()
                 or string.isdigit() or string.isspace()))


def building(string: str):
    """
        print the number of
            - uppercase letters
            - lowercase letters
            - punctuation marks
            - sapces
            - digits
    """
    print(f"The text contains {len(string)} characters:")
    print(f"{sum(1 for s in string if s.isupper())} upper letters")
    print(f"{sum(1 for s in string if s.islower())} lower letters")
    print(f"{sum(1 for s in string if ispunct(s))} punctuation marks")
    print(f"{sum(1 for s in string if s.isspace())} spaces")
    print(f"{sum(1 for s in string if s.isdigit())} digits")


def main():
    """
        execute the building function for
            - an argument if exist (only one)
            - the user input text if no argument is provided 
    """
    if (len(sys.argv) > 2):
        print("AssertionError: more than one argument is provided")
    elif (len(sys.argv) == 2):
        building(sys.argv[1])
    else:
        user_input: str = ""
        try:
            print("What is the text to count?")
            while 1:
                user = input()
                user_input += user + '\n'
        except EOFError:
            pass
        except KeyboardInterrupt:
            print("")
        building(user_input)


if __name__ == "__main__":
    main()
