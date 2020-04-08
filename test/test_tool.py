import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from extractor import check_character, fix_common_mistakes, analyze

def test_check_character():
	"""
	Test if given a sentence returns True if it finds an invalid characther

	Parameters: None

	Returns: None
	"""

	assert check_character("Јас сакам да имам куче.") == False
	assert check_character("I love to have a dog.") == True
	assert check_character("I have 234234 points.") == True


def test_fix_common_mistakes():
	"""
	Test if given a sentence returns True if it finds an invalid characther

	Parameters: None

	Returns: None
	"""

	assert fix_common_mistakes("јас сакам да имам куче.") == "Јас сакам да имам куче."
	assert fix_common_mistakes("Јас незнам да пишувам.") == "Јас не знам да пишувам."
	assert fix_common_mistakes("Ова е компир.") == "Ова е компир."


def test_analyze():
	"""
	Test if given a sentence returns True if it finds an invalid characther

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

