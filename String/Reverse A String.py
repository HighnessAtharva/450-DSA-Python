def reverseString(string):
    str1=str()
    i=len(string)-1
    while i>=0:
        str1+=string[i]
        i-=1
    return str1

# def reverseString2(string):
#     return string[::-1]

print(reverseString("Hell There"))