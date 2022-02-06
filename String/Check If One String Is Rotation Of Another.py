"""
Given a string s1 and a string s2, write a snippet to say whether s2 is a rotation of s1? 
(eg given s1 = ABCD and s2 = CDAB, return true, given s1 = ABCD, and s2 = ACBD , return false)

Algorithm: areRotations(str1, str2)

1. Create a temp string and store concatenation of str1 to str1 in temp. (temp = str1+str1)
2. If str2 is a substring of temp then str1 and str2 are rotations of each other.

Example:                 
str1 = "ABACD"
str2 = "CDABA"
temp = str1+str1 = "ABACDABACD"

Since str2 is a substring of temp, str1 and str2 are 
rotations of each other.
"""

def areRotations(string1, string2):
    if len(string1)!=len(string2):
        return f'{string1} is NOT a rotation of {string2}'
    
    temp=str()
    temp = string1+string1 # remember to duplicate string1 twice and not string1+string2
    return f'{string1} is a rotation of {string2}' if string2 in temp else  f'{string1} is NOT a rotation of {string2}'
        
print(areRotations("CDAA", "ACDA"))
print(areRotations("ADCA", "ACDA"))

