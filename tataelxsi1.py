s='aabbbbeeeeffggg'
lst=[]
newstr=''
for i in s:
    if i not in lst:
        lst.append(i)
        x=s.count(i)
        newstr=newstr+i+str(x)
    else:
        continue
print(newstr)