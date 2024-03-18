d=int(input())
s=input()
mydict={}
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        x=s[i:j]
        y=x[::-1]
        if x==y:
            z=len(x)
            mydict[x]=z
m=list(mydict.values())
n=max(m)
k=m.index(n)
o=(list(mydict.keys()))[k]
print(n)
print(o)
