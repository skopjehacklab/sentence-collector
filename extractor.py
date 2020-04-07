from time import time
import fileinput
import re

# Packed config of variables used in the program
config = {
	"MAX_WORDS": 14,
	"MIN_WORDS": 2,
	"WHITELISTED_CHARACTERS": list("абвгдѓеѐжзѕиѝјклљмнњопрстќуфхцчџшАБВГДЃЕЀЖЗЅИЍЈКЛЉМНЊОПРСТЌУФХЦЧЏШ;„“.?!(),—-: "),
	"SPLIT_INTO_SENTENCES": "(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s",
	"COMMON_MISTAKES": {
		"Сеуште": "Сѐ уште",
		"сеуште": "сѐ уште",
		"Незнам": "Не знам",
		"незнам": "не знам",
		"Одприлика": "Отприлика",
		"одприлика": "отприлика",
		"Сметат": "Сметаат",
		"сметат": "сметаат",
	}
}

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
		if character not in config["WHITELISTED_CHARACTERS"]:
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
		if index == 0 and word.islower():
			sentence = sentence.replace(word, word.capitalize())
		
		if word in config["COMMON_MISTAKES"]:
			sentence = sentence.replace(word, config["COMMON_MISTAKES"][word])

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
		
		# Any digits?
		if bool(re.search('[\d-]', sentence)):
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
	""" Takes a list of sentences and prints them to stdout

	Parameters:
		sentences (list[str]): List of sentences

	Returns:
		None  
	"""
	for sentence in valid_sentences:
		print(f"{sentence}")

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
		sentences = re.split(config["SPLIT_INTO_SENTENCES"], line)
		valid_sentences = analyze(sentences)

		to_stdout(valid_sentences)

	return None

main()
