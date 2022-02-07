# Python program function to find Number of customers who
# could not get a computer
def runCustomerSimulation(n, seq):
    # seen[i] = 0, indicates that customer 'i' is not in cafe
    # seen[1] = 1, indicates that customer 'i' is in cafe but computer is not assigned yet.
    # seen[2] = 2, indicates that customer 'i' is in cafe and has occupied a computer.
    MAX_CHAR=26
    seen=[0]*MAX_CHAR
    res=0
    occupied=0
    for i in range(len(seq)):
        ind=ord(seq[i])-ord('A')
        if seen[ind]==0:
            seen[ind]=1
            if occupied<n:
                occupied+=1
                seen[ind]=2
            else:
                res+=1
        else:
            if seen[ind]==2:
                occupied-=1
            seen[ind]=0

    return res

print (runCustomerSimulation(2, "ABBAJJKZKZ"))
print (runCustomerSimulation(3, "GACCBDDBAGEE"))
print (runCustomerSimulation(3, "GACCBGDDBAEE"))
print (runCustomerSimulation(1, "ABCBCA"))
print (runCustomerSimulation(1, "ABCBCADEED"))