def longestPalindrome(S):
    fi = fj = 0
    n = len(S)

    for i in range(n):
        
        # odd length palindrome with current index as center
        j = i - 1
        k = i + 1
        while j >= 0 and k < n:
            if S[j] != S[k]:
                break
            j -= 1
            k += 1
        if k-j-1 > fj-fi+1:
            fi = j + 1
            fj = k - 1

        # even length palindrome if possible
        if i < n-1 and S[i] == S[i+1]:
            j = i - 1
            k = i + 2
            while j >= 0 and k < n:
                if S[j] != S[k]:
                    break
                j -= 1
                k += 1
            if k-j-1 > fj-fi+1:
                fi = j + 1
                fj = k - 1

    return S[fi:fj+1], f'Length of Longest Palindrome: {len(S[fi:fj+1])}'

print(longestPalindrome('forgeeksskeegfor'))