import config
import fileinput
import re

"""
Takes a sentence and iterates over the characters to find 
if there are any characters that are not in the whitelist.
"""
def check_character(sentence):
	for character in sentence:
		if character not in config.WHITELISTED_CHARACTERS:
			return True
	return False

"""
Takes in a sentence and replaces words that are part of the 
common_mistakes dictionary.
"""
def fix_common_mistakes(sentence):
    for word in sentence.split(" "):
        if word in config.COMMON_MISTAKES:
            sentence = sentence.replace(word, config.COMMON_MISTAKES[word])
        else:
            pass

    return sentence

"""
Takes a list of sentences and for each sentences
checks if it passes the requirements, i.e. no more than 14 words, 
no blacklisted characters etc.
"""
def analyze(sentences):
	valid_sentences = []

	for sentence in sentences:
		# Any invalid characters?
		if check_character(sentence):
			continue
		
		# Any digits?
		if bool(re.search('[\d-]', sentence)):
			continue

		# More than 14 words?
		if len(sentence.split(' ')) > config.MAX_WORDS:
			continue

		# If all of these passed, finally check for common mistakes
		sentence = fix_common_mistakes(sentence)

		valid_sentences.append(sentence)
	
	return valid_sentences

"""
Takes a list of all valid sentences and writes
it into a file with a new line appended after each sentence
"""
def write_to_file(valid_sentences):
	with open(config.OUTPUT_FILE, 'w') as w:
		for sentence in valid_sentences:
			w.write(f"{sentence}\n")

def main():
	all_time_valid_sentences = 0

	received_lines = fileinput.input()
	
	for index, line in enumerate(received_lines):
		sentences = re.split(config.SPLIT_INTO_SENTENCES, line)
		valid_sentences = analyze(sentences)

		all_time_valid_sentences += len(valid_sentences)
	
		write_to_file(valid_sentences)

	print(f"Found {all_time_valid_sentences - 1} valid sentences. All of them were extracted to {config.OUTPUT_FILE}")
	return None

main()
