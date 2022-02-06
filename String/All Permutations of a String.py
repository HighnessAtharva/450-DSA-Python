def permute(s, answer):
    if len(s)==0:
        print(answer, end=' ')
        return 
    
    for i in range(len(s)):
        ch=s[i]
        left=s[0:i]
        right=s[i+1:]
        rest=left+right
        permute(rest, answer+ch)

answer=str()
print(permute("ABC", answer))