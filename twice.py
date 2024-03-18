def twice(lst):
    r=[]
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]==lst[j]:
                r.append(lst[i])
    x=set(lst)-set(r)
    return list(x)
    

result=twice([6,1,2,4,2,6,4])
print(result)