def minimumNumberOfSwaps(S):
        swap=0
        imbalance=0
        countLeft=0
        countRight=0
        for i in range(len(S)):
            if S[i] == '[':
                countLeft+=1
                if imbalance > 0: 
                    swap += imbalance;  
                    imbalance-=1    

            elif S[i] == ']':  
                countRight+=1 
                imbalance = (countRight-countLeft);  
        return swap

print(minimumNumberOfSwaps('[]][]['))