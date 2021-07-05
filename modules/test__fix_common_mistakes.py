from fix_common_mistakes import fix_common_mistakes

case_one_short = "Све е тоа панк."
case_one_valid = "Сѐ е тоа панк."

assert fix_common_mistakes(case_one_short) == case_one_valid
assert fix_common_mistakes(case_one_short) != case_one_short

case_two_short = "Незнам како се вика девојката."
case_two_valid = "Не знам како се вика девојката."

assert fix_common_mistakes(case_two_short) == case_two_valid
assert fix_common_mistakes(case_two_short) != case_two_short

case_three_short = "Не дошле резултатите сеуште."
case_three_valid = "Не дошле резултатите сѐ уште."

assert fix_common_mistakes(case_three_short) == case_three_valid
assert fix_common_mistakes(case_three_short) != case_three_short
