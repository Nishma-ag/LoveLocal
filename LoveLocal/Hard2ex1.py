def shortestPalindrome(s):
    n = len(s)
    i = 0

    
    for j in range(n - 1, -1, -1):
        if s[i] == s[j]:
            i += 1

    if i == n:
        return s

    suffix = s[i:]
    prefix = s[:i][::-1]

    return prefix + s

s = "aacecaaa"
output = shortestPalindrome(s)
print(output)
