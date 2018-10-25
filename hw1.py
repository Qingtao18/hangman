
# -*- coding: utf-8 -*
#!/usr/bin/python
import os
import sys
length = 5
words = []
freq = []
dict = {} #original data
with open('hw1_word_counts_05.txt', 'r') as f: #read the word and its frequency	
	for line in f.readlines():
		lineData = line.strip('\n').split(' ') #delet'/n' in each line, then store the word and frequency seperatly and also correspondingly in a dictionary
		words.append(lineData[0])
		freq.append(int(lineData[1]))
		dict[lineData[0]] = int(lineData[1]);
totalCount = sum(freq)
priorProb = {} #prior probabilities
for word in words:
	f = dict.get(word)
	priorProb[word] = float(f)/float(totalCount)

"""
#answer to (a)
# for (a), sort the dictionary
sortedDict = sorted(dict.items(),key=lambda d:d[1])

print 'The fifteen most frequent 5-letter words are:' 
for element in sortedDict[-15:]:
	print element[0],
print 
print 'The fourteen least frequent 5-letter words are :' 
for element in sortedDict[0:14]:
	print element[0],
print
"""
# answer to (b)
num = len(words)

incorrectlyGuess = ['O','D','L','C']#set of incorrectly guesses, now implies {O, D, L, C}
correctlyGuess = ['','','U','','']#set of correctly guessed, now implies – – U – –
guess = [0 for n in range(26)]#The probs of 26 character in next guess
conditionalProbs = [-1 for n in range(num)]; #P(E|W =w)P(W =w) for now

for i in range(num):
	word = words[i]
	for j in range(length):
		if correctlyGuess[j] != '':
			if word[j] != correctlyGuess[j]:#P(E|W =w) = 0 for words has different character in correctly guessed positions
				conditionalProbs[i] = 0;
				break;
		else:
			for k in correctlyGuess: 
				if word[j] == k:#P(E|W =w) = 0 for words has correctly guessed character in other positions except showed ones
					conditionalProbs[i] = 0;
					break;
		for incorrectW in incorrectlyGuess:
			if word[j] == incorrectW:#P(E|W =w) = 0 for words has incorrectly guessed character
				conditionalProbs[i] = 0;
				break;
	if conditionalProbs[i] != 0:
		conditionalProbs[i] = priorProb[word]
		#print word
totalProb = sum(conditionalProbs)#􏰆 sum of P(E|W =w′)P(W =w′) for all w'
charaDict = {}#set of character showed in possible words, using dictionary just in case if there are repeat characters in a word

for i in range(num):
	if conditionalProbs[i] != 0:
		conditionalProbs[i] = conditionalProbs[i]/totalProb #P(W =w|E)
		word = words[i]
		for j in range(length):
			if correctlyGuess[j] == '':
				charaDict[word[j]] = 1
		for chara in charaDict:#for each possible word of answer, probs of all the character in the next guess except guessed ones need to add P(W =w|E)
			guess[ord(chara) - ord('A')] += conditionalProbs[i]
	charaDict = {}#clear the dictionary
index = guess.index(max(guess))#index of best next guess
print 'Best next guess l is :'
print chr(index + ord('A'))
print 'The prob for best next guess P(Li=l for some i∈{1,2,3,4,5}|E) = '
print max(guess)
