from extractor import check_character, fix_common_mistakes, analyze

def test_check_character():
	"""
	Test if given a sentence returns True if it finds an invalid character and False if it finds valid

	Parameters: None

	Returns: None
	"""

	assert check_character("Јас сакам да имам куче.") == False
	assert check_character("I love to have a dog.") == True
	assert check_character("Јас имам 234234 поена.") == True


def test_fix_common_mistakes():
	"""
	Test if given a sentence it'll return a correct form of it.

	Parameters: None

	Returns: None
	"""

	assert fix_common_mistakes("јас сакам да имам куче.") == "Јас сакам да имам куче."
	assert fix_common_mistakes("Јас незнам да пишувам.") == "Јас не знам да пишувам."
	assert fix_common_mistakes("Ова е компир.") == "Ова е компир."


def test_analyze():
	"""
	Test if given a list of sentences it'll return the valid ones.
	
	Parameters: None

	Returns: None
	"""
	sentences = [
		"",
		"I love to have a dog.",
		"Знаеш?",
		"Знаеш ли друже што ми се деси нема да веруваш леле чоек како не беше таму.",
		"Сакам да си одам дома."
	]

	validSentences = [
		"Сакам да си одам дома."
	]

	assert analyze(sentences) == validSentences


