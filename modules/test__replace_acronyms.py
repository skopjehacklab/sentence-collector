from replace_acronyms import replace_acronyms

case_one_short = "Претставата од МНТ ќе ја даваат на МТВ."
case_one_valid = "Претставата од Македонски народен театар ќе ја даваат на Македонска телевизија."

assert replace_acronyms(case_one_short) == case_one_valid
assert replace_acronyms(case_one_short) != case_one_short

case_two_short = "ОН се една огромна ..."
case_two_valid = "Обединети нации се една огромна ..."

assert replace_acronyms(case_two_short) == case_two_valid
assert replace_acronyms(case_two_short) != case_two_short

case_three_short = "Сѐ е тоа заслуга на ОН."
case_three_valid = "Сѐ е тоа заслуга на Обединети нации."

assert replace_acronyms(case_three_short) == case_three_valid
assert replace_acronyms(case_three_short) != case_three_short
