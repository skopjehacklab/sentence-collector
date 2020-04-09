from time import time
import fileinput
import re
import json

# Packed config of variables used in the program
config = {
	"MAX_WORDS": 14,
	"MIN_WORDS": 2,
	"DICTIONARY_FILE": "dictionary.json",
	"SPLIT_INTO_SENTENCES": "(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s",
}

def parse_dictionary(file_name) -> dict:
	""" Takes a file name, reads parses the JSON 
	content and returns a dictionary

	Parameters:
			file_name (str): the name of the file

	Returns:
			dictionary (dict): parsed json content
	"""
	with open(file_name, 'r') as f:
	    dictionary = json.load(f)

	return dictionary

dictionary = parse_dictionary(config["DICTIONARY_FILE"])

def check_character(sentence) -> bool:
	""" Given a sentence, returns True if it finds an invalid character,
	False otherwise

	Parameters:
		sentence (str): A sentence

	Returns:
		True (bool): If there is a not white-listed character in the sentence
		False (bool): If all characters are valid and white-listed   
	"""
	for character in sentence:
		if character not in dictionary["WHITELISTED_CHARACTERS"]:
			return True
	return False


def fix_common_mistakes(sentence) -> str:
	""" Loops through the words of a given sentence and replaces all words that 
	are part of the config['COMMON_MISTAKES'].

	Parameters:
		sentence (str): A sentence

	Returns:
		sentence (str): The same, or fixed sentence   
	"""
	for index, word in enumerate(sentence.split(" ")):
		word_is_uppercase = word[0].isupper()

		if index == 0 and word.islower():
			sentence = sentence.replace(word, word.capitalize())
			word_is_uppercase = True

		if word_is_uppercase and word.lower() in dictionary["COMMON_MISTAKES"]:
			sentence = sentence.replace(word.capitalize(), dictionary["COMMON_MISTAKES"][word.lower()].capitalize())

		if not word_is_uppercase and word.lower() in dictionary["COMMON_MISTAKES"]:
			sentence = sentence.replace(word.lower(), dictionary["COMMON_MISTAKES"][word])

	return sentence

def analyze(sentences) -> list:
	""" Analyzes given sentences and returns only the valid ones.

	Parameters:
		sentences (list[str]): List of sentences

	Returns:
		valid_sentences (list[str]): List of valid sentences   
	"""
	valid_sentences = []

	for sentence in sentences:
		# Empty field?
		if not sentence:
			continue

		# Any invalid characters?
		if check_character(sentence):
			continue

		# More than 14 words and less than 2 words?
		words_length = len(sentence.split(' '))
		if words_length > config["MAX_WORDS"] or words_length < config["MIN_WORDS"]:
			continue

		# If all of these passed, finally check for common mistakes
		sentence = fix_common_mistakes(sentence)

		valid_sentences.append(sentence)
	
	return valid_sentences

def to_stdout(valid_sentences) -> None:
	""" Takes a list of valid sentences and outputs them to stdout

	Parameters:
		valid_sentences (list[str]): List of sentences

	Returns:
		None  
	"""
	for sentence in valid_sentences:
		print(f"{sentence}")

def replace_abbreviations(line) -> str:
	""" Takes a line, finds all of the 
	shortened form of a written word and replaces them
	with their full form.

	Parameters:
			line (str): set of characters

	Returns:
			line (str): set of characters
	"""

	# Can be optimized
	for abbreviation in dictionary["ABBREVIATIONS"]:
		if abbreviation or abbreviation.capitalize() in line:
			line = line.replace(abbreviation.capitalize(), dictionary["ABBREVIATIONS"][abbreviation].capitalize())
			line = line.replace(abbreviation, dictionary["ABBREVIATIONS"][abbreviation])

	return line

def main() -> None:
	""" Program main. Loops through the received lines of text from
	stdin, and calls the needed functions in order to extract 
	valid sentences. Outputs information about the sentences and
	where they extracted.

	Parameters:
		None

	Returns:
		None 
	"""
	received_lines = fileinput.input()

	for index, line in enumerate(received_lines):
		line = replace_abbreviations(line)

		sentences = re.split(config["SPLIT_INTO_SENTENCES"], line)
		valid_sentences = analyze(sentences)

		to_stdout(valid_sentences)

	return None

if __name__ == '__main__':
    main()

