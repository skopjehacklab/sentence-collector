from replace_abbreviations import replace_abbreviations

case_one_short = "Направена во 1991 г."
case_one_valid = "Направена во 1991 година."

assert replace_abbreviations(case_one_short) == case_one_valid
assert replace_abbreviations(case_one_short) != case_one_short

case_two_short = "Тој е роден во 1991 год. во Белград."
case_two_valid = "Тој е роден во 1991 година во Белград."

assert replace_abbreviations(case_two_short) == case_two_valid
assert replace_abbreviations(case_two_short) != case_two_short

case_three_short = "Утре е празникот св. Илија."
case_three_valid = "Утре е празникот свети Илија."

assert replace_abbreviations(case_three_short) == case_three_valid
assert replace_abbreviations(case_three_short) != case_three_short

case_four_short = "Јас учам на универзитетот Св. Кирил и Методиј."
case_four_valid = "Јас учам на универзитетот Свети Кирил и Методиј."

assert replace_abbreviations(case_four_short) == case_four_valid
assert replace_abbreviations(case_four_short) != case_four_short
