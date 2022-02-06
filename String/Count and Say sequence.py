def countAndSay(n):
   s = "1"
   if n == 1:
      return s

   for i in range(2,n+1):
      i, count = 0, 0 #initialize to zero
      temp, curr = str(), str() #initialize as empty strings
      
      while i<len(s):
         if curr =="":
            curr=s[i]
            count=1
            i+=1
         elif curr == s[i]:
            count+=1
            i+=1
         else:
            temp+= str(count) + curr
            curr=""
            count = 0
      
      temp+=str(count) + curr
      s=temp

   # return s after the final iteration
   return s

print(countAndSay(6))