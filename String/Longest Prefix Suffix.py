#Given a string s, find the length of the longest prefix, which is also a suffix. The prefix and suffix should not overlap.

def longestPrefixSuffix(s) :
    n = len(s)
    for i in range(n//2, 0, -1):
        prefix = s[0:i]
        suffix = s[n-i: n]
        if (prefix == suffix):
            return i, prefix # can also return i, suffix
    return 0

print(longestPrefixSuffix("blablabla"))