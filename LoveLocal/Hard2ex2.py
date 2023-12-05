def shortestPalindrome(s):
    n = len(s)
    i = n - 1


    while i >= 0 and s != s[::-1]:
        i -= 1

    if i == -1:
        return s

    suffix = s[i + 1:]
    prefix = s[:i + 1][::-1]

    return prefix + s

s = "abcd"
output = shortestPalindrome(s)
print(output)
