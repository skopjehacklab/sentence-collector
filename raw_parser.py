from os import walk
from os.path import isfile, join
import html2text
import re

blacklistedFiles = ['sentences.txt']
addedSentences = []
blacklistedCharacthers = ['*', '//', '#', '{', '}', '::', 'json', '[', ']', '(', ')', '=']
searchFolder = 'makedonskijazik.mk'


def checkCharacther(sentence):
	for index, characther in enumerate(blacklistedCharacthers):
		if characther in sentence:
			return True
	return False

with open('raw_sentences.txt','a') as f:
	for root, subdirs, files in walk(searchFolder):
		for fileindex, visitFile in enumerate(files):
			if visitFile not in blacklistedFiles:
				file = join(root, visitFile)
				try:
					fro = open(file,'r')
					frc = fro.read()
					print(f"\033[92m [+] Scrapping {file} for sentences \033[0m")
					scraper = html2text.HTML2Text()
					scraper.ignore_links = True
					scraper.ignore_emphasis = True
					scraper.ignore_images = True
					scraper.ignore_tables = True
					data = scraper.handle(frc)
					#data = data.replace('/','').replace('_','')
					data = re.sub('[\d-]','',data)
					sentences = data.split('.')
					for ind, sentence in enumerate(sentences):
						if not checkCharacther(sentence) and sentence not in addedSentences:
							f.write(sentence)
							addedSentences.append(sentence)
				except IsADirectoryError:
					print(f"\033[94m [+] Encountered folder {file}! Skipping... \033[0m")
				except UnicodeDecodeError:
					print(f"\033[91m [+] Failed parsing {file}! Skipping... \033[0m")

print(f"\033[92m [+] Finished scraping for sentences! Sentences can be found at raw_sentences.txt \033[0m")
