def isBalanced(string):
    stack=[]
    for char in string:
        if char in ["[","{","("]:
            stack.append(char)
        else:
            # IF current character is not opening bracket, then it must be closing. So stack cannot be empty at this point.
            if not stack:
                return False
            
            current=stack.pop()
            if current=="(":
                if char != ")":
                    return False
            if current=="[":
                if char!="]":
                    return False
            if current== "(":
                if char!=")":
                    return False
    # After popping all the characters check if Empty Stack
    if stack:
        return False
    return True

if isBalanced('{({}[])}[]'):
    print("Balanced")
else:
    print("Not Balanced")