class Solution:
    def reverseWords(s):
        l1=s.split()
        l1.reverse()
        return " ".join(l1)
    
    x=reverseWords("welcome     to jungle  ")
    print(x)