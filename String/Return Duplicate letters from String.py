#Print all the duplicates and their counts in the input string 

from collections import defaultdict
 
def printDuplicates(string):
    count = defaultdict(int)
    for i in string:
        # Skipping checks for spaces and tabs
        if i==' ' or i=='\t': 
            continue
        count[i] += 1
    
    for key in count:
        if (count[key] > 1):
            print(f'{key} appears {count[key]} times')
 

printDuplicates('Testing for duplicate characters in this string')