import unicodedata, string
from string import ascii_letters

def remove_accents(data):
	return unicodedata.normalize('NFKD', data).encode('ASCII', 'ignore')

with open("base.tsv", "r") as input:
	with open("new_sample.tsv", "w") as output:
		for line in input:
			words = line.rstrip("\n").split("\t")
			words_ascii = []
			for word in words:
				words_ascii.append(remove_accents(word).decode("utf-8"))
			string = '\t'.join(words_ascii) + '\n'
			output.writelines(string)
