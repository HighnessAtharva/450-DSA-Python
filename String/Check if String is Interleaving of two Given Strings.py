# Given three strings, return true if the third string is interleaving the first and second strings, i.e., it is formed from all characters of the first and second string, and the order of characters is preserved.
# For example:-
# ACDB is interleaving of AB and CD
# ADEBCF is interleaving of ABC and DEF
# ACBCD is interleaving of ABC and CD
# ACDABC is interleaving of ABC and ACD

def isInterleaving(X, Y, S):
    if not X and not Y and not S:
        return True
        
    if not S:
        return False

    # check for x
    x= (len(X) and X[0]==S[0]) and (isInterleaving(X[1:], Y, S[1:]))
    # check for y
    y= (len(Y) and S[0]==Y[0]) and (isInterleaving(X, Y[1:], S[1:]))

    return x or y

# TestCase1
if isInterleaving('ABC', 'DEF', 'ADEBCF'):
    print('Interleaving')
else:
    print('Not Interleaving')

# TestCase2
if isInterleaving('ABC', 'DEF', 'ADECFB'):
    print('Interleaving')
else:
    print('Not Interleaving')

# TestCase3
if isInterleaving('ABC', 'DEF', 'ADFBEC'):
    print('Interleaving')
else:
    print('Not Interleaving')