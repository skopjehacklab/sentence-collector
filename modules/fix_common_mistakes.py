import fileinput
from config import config as cfg
from utils import parse_dictionary, isAlpha, to_stdout

dictionary = parse_dictionary(cfg["DICTIONARY_FILE"])

def fix_common_mistakes(line) -> None:
    for word in line.split(" "):
        if not isAlpha(word):
            break

        if "." in word: # Во случај да е последниот збор
            word = word.strip(".")

        if word in dictionary["COMMON_MISTAKES"]:
            line = line.replace(word, dictionary["COMMON_MISTAKES"][word])

        if word[0].isupper() and not word.isupper() and word.lower() in dictionary["COMMON_MISTAKES"]:
            replaced = dictionary["COMMON_MISTAKES"][word.lower()].capitalize()
            line = line.replace(word, replaced)
    
    return line

def main() -> None:
    lines = []

    for line in fileinput.input():
        line = line.rstrip() # избриши ги: \n
        line = lines.append(fix_common_mistakes(line))

    to_stdout(lines)

if __name__ == '__main__':
    main()

