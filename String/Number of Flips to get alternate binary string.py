#Given a binary string, that is it contains only 0s and 1s. We need to make this string a sequence of alternate characters by flipping some of the bits, our goal is to minimize the number of bits to be flipped. 
# Input : str = “001”
# Output : 1
# Minimum number of flips required = 1
# We can flip 1st bit from 0 to 1 


def flip( ch):
    return '1' if (ch == '0') else '0'
 
# Utility method to get minimum flips when
# alternate string starts with expected char
def getFlipWithStartingCharcter(str, expected):
    flipCount = 0
    for i in range(len( str)):
        
        # if current character is not expected, increase flip count
        if (str[i] != expected):
            flipCount += 1
 
        # flip expected character each time
        expected = flip(expected)
    return flipCount
 
# method return minimum flip to make binary
# string alternate
def minFlipToMakeStringAlternate(str):
    return min(getFlipWithStartingCharcter(str, '0'),getFlipWithStartingCharcter(str, '1'))
 

str = "0001010111"
print(minFlipToMakeStringAlternate(str))