def reverseWords(s):
    return ' '.join(s.split(' ')[-1::-1])

"""This is basically what the function above does"""
# def reverseWords2(s):
#     list1=list()
#     list1=s.split(' ')[-1::-1]
#     return (' '.join(list1))

print(reverseWords('Sharingan is the best jutsu'))