import fileinput
import re

blacklistedCharacthers = ['*', '//', '#', '{', '}', '::', 'json', '[', ']', '(', ')', '=', 'X', 'I', 'V', 'L', 'C', 'D', 'M']
outputFile = 'sentences.txt'

mistakes = {
  "сеуште": "сѐ уште",
  "незнам": "не знам",
  "сметат":"сметаат"
  }

def checkCharacther(sentence):
	for index, characther in enumerate(blacklistedCharacthers):
		if characther in sentence:
			return True
	return False

text = ""

for line in fileinput.input():
	text+=line

if text is "":
	print("\033[91m [+] No text has been found. Exitting... \033[0m")


print("\033[94m [+] Splitting file into sentences... \033[0m")
sentences = re.split("(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", text)

with open(outputFile, 'a') as f:
	for index, line in enumerate(sentences):
		if not checkCharacther(line) and not bool(re.search('[\d-]' ,line)) and len(line.split(' ')) <= 14:
			f.write(f"{line}\n")

print(f"\033[92m [+] Process Complete. Output can be found at {outputFile}... \033[0m")