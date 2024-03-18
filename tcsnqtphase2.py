def sum(lst):
    mydict={}
    for i in range(len(lst)):
        total=0
        for j in range(i,len(lst)):
            total+=lst[j]
            if total not in mydict:
                mydict[total]=lst[i:j+1]
    x=dict(sorted(mydict.items()))
    y=max(list(sorted(mydict.keys())))
    z=x[y]
    return z
                       
    
result=sum([7,-4,2,-1,4])
print(result)