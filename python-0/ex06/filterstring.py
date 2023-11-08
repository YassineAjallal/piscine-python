from ft_filter import ft_filter
import sys


def filterstring(string: str, max: int) -> list:
    str_list = string.split()
    return list(ft_filter(lambda x: len(x) > max, str_list))


def valid_string(string: str) -> int:
    return sum(1 for s in string if (s.isalnum() or s.isspace()))


def main():
    integer: int
    if len(sys.argv) > 3:
        print("AssertionError: more than two argument is provided")
    elif len(sys.argv) < 3:
        print("AssertionError: the arguments are bad")
    else:
        try:
            integer = int(sys.argv[2])
            if (valid_string(sys.argv[1]) != len(sys.argv[1])):
                print("AssertionError: the arguments are bad")
            else:
                print(filterstring(sys.argv[1], integer))
        except ValueError:
            print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
