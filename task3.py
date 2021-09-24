import sys
import re

if len(sys.argv) > 1:
	path = sys.argv[1]
else:
	path = "task3_data.txt"
file = open(path)
words = dict()
maxword = ""
for line in file:
	line = re.sub(r'[^\w\s]','',line)
	for word in line.split():
		if word.isalpha():
			if len(word) > len(maxword):
				maxword = word 
			if word in words:
				words[word] += 1
			else:
				words[word] = 1
populatedword = ""
maxpopulation = 0
for word in words.keys():
	if words[word] > maxpopulation:
		populatedword = word
		maxpopulation = words[word]
print("Самое длинное слово:", maxword, "(длина:", len(maxword),")")
print("Наиболее часто встречающееся слово:", populatedword,"(встречается", maxpopulation,"раз)")

