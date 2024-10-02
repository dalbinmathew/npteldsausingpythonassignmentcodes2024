# Split string into three palindromic substrings with earliest possible cuts

# Given string str, the task is to check if it is possible to split the 
# given string S into three palindromic substrings or not. If multiple 
# answers are possible, then print the one where the cuts are made the 
# least indices. If no such possible partition exists, then print “-1”.

# Input: str = “aabbcdc”
# Output: aa bb cdc
# Explanation:
# Only one possible partition exists {“aa”, “bb”, “cdc”}.

# Input: str = “ababbcb”
# Output: a bab bcb 
# Explanation: Possible splits are {“aba”, “b”, “bcb”} and {“a”, “bab”, “bcb”}. 
# Since, {“a”, “bab”, “bcb”} has splits at earlier indices, it is the required answer.


def isPalindrome(s):
    if len(s)==1:
        return True
    s1=s[::-1]
    return s1==s


def solve(s):
	n = len(s)	 
	for i in range(1,n-2):
		s1 = s[:i]
		if isPalindrome(s1):
			for j in range(i+1,n):
       #for nte ullil n 9 aanenkil, 8 vare loop cheyyuvollu
       #apo s2 [i:j] vekkumbo j 8 vannalum, 7th character vare slicing il pedu (indexing from zero)
				s2 = s[i:j]
				s3 = s[j:]
				if isPalindrome(s2) and isPalindrome(s3):
					print(s1, s2, s3)
					return
	print(-1)
	
s = "aaaabaaaa"
solve(s)
