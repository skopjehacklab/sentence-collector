import fileinput
from config import config as cfg
from utils import parse_dictionary, isAlpha, to_stdout

dictionary = parse_dictionary(cfg["DICTIONARY_FILE"])

def replace_acronyms(line) -> str:
    words = line.split(" ")

    for word in words:
        if not isAlpha(word):
            continue

        if "." in word:
            word = word.strip(".")
        
        # Сите акроними се со големи букви
        if word.isupper() and word in dictionary["ACRONYMS"]:
            line = line.replace(word, dictionary["ACRONYMS"][word])

    return line

def main() -> None:
    lines = []

    for line in fileinput.input():
        line = line.rstrip() # избриши ги: \n
        line = lines.append(replace_acronyms(line))

    to_stdout(lines)

if __name__ == '__main__':
    main()
