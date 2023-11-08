import sys

NESTED_MORSE = {
    " ": "/ ",
    'A': '.- ',
    'B': '-... ',
    'C': '-.-. ',
    'D': '-.. ',
    'E': '. ',
    'F': '..-. ',
    'G': '--. ',
    'H': '.... ',
    'I': '.. ',
    'J': '.--- ',
    'K': '-.- ',
    'L': '.-.. ',
    'M': '--',   
    'N': '-. ',
    'O': '--- ',
    'P': '.--. ',
    'Q': '--.- ',
    'R': '.-. ',
    'S': '... ',
    'T': '- ',
    'U': '..- ',
    'V': '...- ',
    'W': '.-- ',
    'X': '-..- ',
    'Y': '-.-- ',
    'Z': '--.. ',
    '0': '----- ',
    '1': '.---- ',
    '2': '..--- ',
    '3': '...-- ',
    '4': '....- ',
    '5': '..... ',
    '6': '-.... ',
    '7': '--... ',
    '8': '---.. ',
    '9': '----. ',
}

def valid_string(string: str) -> int:
    return sum(1 for s in string if (s.isalnum() or s == ' '))


def morse(string: str) -> str:
    return [NESTED_MORSE[s.upper()] for s in string]

def main():
    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
    else:
        if valid_string(sys.argv[1]) != len(sys.argv[1]):
            print("AssertionError: the arguments are bad")
        else:
           print(''.join(morse(sys.argv[1])))

if __name__ == "__main__":
    main()