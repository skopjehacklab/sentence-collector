import json

ALPHABET = "абвгдѓеѐжзѕиѝјклљмнњопрстќуфхцчџшАБВГДЃЕЀЖЗЅИЍЈКЛЉМНЊОПРСТЌУФХЦЧЏШ"
WHITELISTED_CHARACTERS = ALPHABET + ";„“.?!,-—: "

def parse_dictionary(file_name) -> dict:
	with open(file_name, 'r') as f:
	    dictionary = json.load(f)

	return dictionary

def character_is_whitelisted(sentence):
    for character in sentence:
        if character not in WHITELISTED_CHARACTERS:
            return False

    return True

def isAlpha(word) -> bool:
    word = word.strip(".,„“")

    for letter in word:
        if not letter in ALPHABET:
            return False

    return True

def to_stdout(line_list) -> None:
	for line in line_list:
		print(line)
