# Approach: Initialize count = 0 and traverse the string character by character and keep track of the number of 0s and 1s so far, whenever the count of 0s and 1s become equal increment the count. As in the given question, if it is not possible to split string then on that time count of 0s must not be equal to count of 1s then return -1 else print the value of count after the traversal of the complete string.


def maxSubStr(str):
	
	# To store the count of 0s and 1s
	count0 = 0
	count1 = 0
	n = len(str)
	
	# To store the count of maximum substrings str can be divided into
	cnt = 0
	
	for i in range(n):
		if str[i] == '0':
			count0 += 1
		else:
			count1 += 1
		if count0 == count1:
			cnt += 1

# It is not possible to split the string
	if count0 != count1:
		return -1	
	return cnt

print(maxSubStr("0100110101"))
