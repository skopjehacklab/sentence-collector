from extractor import replace_abbreviations, check_character, fix_common_mistakes, analyze


# Test if given a sentence returns True if it finds an invalid character and False if it finds valid
def test_check_character():
	assert check_character("Јас сакам да имам куче.") == False
	assert check_character("I love to have a dog.") == True
	assert check_character("Јас имам 234234 поена.") == True


# Test if given a sentence it'll return a correct form of it.	
def test_fix_common_mistakes():
	assert fix_common_mistakes("јас сакам да имам куче.") == "Јас сакам да имам куче."
	assert fix_common_mistakes("Јас незнам да пишувам.") == "Јас не знам да пишувам."
	assert fix_common_mistakes("Ова е компир.") == "Ова е компир."
	assert fix_common_mistakes("Сеуште незнам како се вика.") == "Сѐ уште не знам како се вика."
	assert fix_common_mistakes("Одприлика уште малце.") == "Отприлика уште малце."


# Test if given a list of sentences it'll return the valid ones.
def test_analyze():
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

# Test if the function replaces abbreviations correctly
def test_replace_abbreviations():
	case_one_short = "Претставата од МНТ ќе ја даваат на МТВ."
	case_one_valid = "Претставата од Македонски народен театар ќе ја даваат на Македонска телевизија."

	assert replace_abbreviations(case_one_short) == case_one_valid
	assert replace_abbreviations(case_one_short) != case_one_short

	case_two_short = "На пр. науката е ..."
	case_two_valid = "На пример науката е ..."

	assert replace_abbreviations(case_two_short) == case_two_valid
	assert replace_abbreviations(case_two_short) != case_two_short

	case_three_short = "на ул. Наум Наумовски Борче."
	case_three_valid = "на улица Наум Наумовски Борче."

	assert replace_abbreviations(case_three_short) == case_three_valid
	assert replace_abbreviations(case_three_short) != case_three_short
