from collections import Counter

def firstRepeatedWord(sentence):
    lis = list(sentence.split(" "))
    frequency = Counter(lis)

    for i in frequency:
        if(frequency[i] > 1):
            return i
 
sentence = "That's a pull-up bitch Don't make me pull up, bitch I'd smash that thot, then pull out bitch"
print(firstRepeatedWord(sentence))