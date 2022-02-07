def wordBreak(wordList, word):
	if word == '':
		return True
	else:
		wordLen = len(word)
		return any([(word[:i] in wordList) and wordBreak(wordList, word[i:]) for i in range(1, wordLen+1)])


wordList={ "i", "like", "sam", "sung", "samsung", "mobile", "ice", 
  "cream", "icecream", "man", "go", "mango"}
word="manmobilecream"
print(wordBreak(wordList, word))