from common_voice_filter import common_voice_filter

case_one_invalid = "Оваа реченица не е дозволена зашто содржи броеви како 1234 и недозволени карактери како @."
case_two_invalid = "Исто така, оваа реченица не е дозволена затоа што содржи повеќе од четиринаесет зборови во неа."

assert common_voice_filter(case_one_invalid) == False
assert common_voice_filter(case_two_invalid) == False

case_three_valid = "Оваа треба да е океј."
case_four_valid = "И оваа."

assert common_voice_filter(case_three_valid) == case_three_valid
assert common_voice_filter(case_four_valid) == case_four_valid

case_five_invalid = "Не."

assert common_voice_filter(case_five_invalid) == False
