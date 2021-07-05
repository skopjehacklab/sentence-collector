import fileinput
from config import config as cfg
from utils import parse_dictionary, isAlpha, to_stdout

dictionary = parse_dictionary(cfg["DICTIONARY_FILE"])

def replace_abbreviations(line) -> str:
    words = line.split(" ")

    for word in words:
        if not isAlpha(word):
            continue

        # Во случај последниот збор да биде кратенка, last се користи подолу
        # да додаде точка.
        last = None
        if word == words[-1] and word in dictionary["ABBREVIATIONS"]:
            last = True

        # Овде бараме дали кратенката е со мали букви (пример: св.) и дали постои во dictionary["ABBREVIATIONS"]
        if word in dictionary["ABBREVIATIONS"]:
            line = line.replace(word, dictionary["ABBREVIATIONS"][word])

        # Овде бараме да дали првата буква на кратенката е со голема буква, а останатите со мали
        # и ако да, ја конвертираме целата кратенка да биде со мали букви за да провериме во 
        # dictionary["ABBREVIATIONS"], ако постои, тогаш ќе ја земеме таа вредност (каде што целиот збор ќе биде со мали букви)
        # и му ја враќаме првата буква да биде голема.
        if word[0].isupper() and not word.isupper() and word.lower() in dictionary["ABBREVIATIONS"]: # можеби има подобар начин да се провери?
            replaced = dictionary["ABBREVIATIONS"][word.lower()].capitalize()
            line = line.replace(word, replaced)
        
        if last:
            line = line + '.'

    return line

def main() -> None:
    lines = []

    for line in fileinput.input():
        line = line.rstrip() # избриши ги: \n
        line = lines.append(replace_abbreviations(line))

    to_stdout(lines)

if __name__ == '__main__':
    main()

