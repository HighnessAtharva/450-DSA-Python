def isPalindrome(s):
    return 'Is a Palindorme' if s == s[::-1] else 'Not a Palindrome'

print(isPalindrome('Hello'))
print(isPalindrome('AAABAAA'))