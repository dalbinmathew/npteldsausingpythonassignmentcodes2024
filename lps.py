def lps(s):
    longest=""
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            test=s[i:j]
            if test==test[::-1]:
                if len(test)>len(longest):
                    longest=test
    return longest

ss="abbabba"
print(lps(ss))
