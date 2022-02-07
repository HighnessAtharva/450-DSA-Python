# Function to find the longest common prefix between two strings
def LCP(X, Y):
    i = j = 0
    while i < len(X) and j < len(Y):
        if X[i] != Y[j]:
            break
        i = i + 1
        j = j + 1
 
    return X[:i]
 
 
# Function to find the longest common prefix (LCP) between a given set of strings
def findLCP(words):
    #intially, set the LCP to first element
    prefix = words[0]

    #traverse the wordslist and set prefix as value returned by Common Prefix between two strings. 
    for s in words:
        prefix = LCP(prefix, s)
    return prefix
 

words = ['techie delight', 'tech', 'techie', 'technology', 'technical']
print('The longest common prefix is', findLCP(words))
 