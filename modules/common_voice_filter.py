from utils import character_is_whitelisted, to_stdout
import fileinput

MAX_WORDS = 14
MIN_WORDS = 2

def common_voice_filter(sentence) -> str:
	sentence = sentence.rstrip() # избриши ги: \n

	words_length = len(sentence.split(' '))

	if words_length > MAX_WORDS or words_length < MIN_WORDS:
		return False

	if not character_is_whitelisted(sentence):
		return False
	
	return sentence

def main() -> None:
	lines = []

	for sentence in fileinput.input():
		sentence = sentence.rstrip() # избриши ги: \n

		sentence = common_voice_filter(sentence)

		if (sentence):
			lines.append(sentence)

	to_stdout(lines)

if __name__ == '__main__':
    main()
