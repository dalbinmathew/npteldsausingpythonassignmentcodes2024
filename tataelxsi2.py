def ispalindrome(s):
    return s == s[::-1]

def solve(s):
    if ispalindrome(s):
        return None
    for i in range(len(s)):
        x = s[:i][::-1]
        if ispalindrome(s + x):
            return x

s = input()
print(solve(s))
