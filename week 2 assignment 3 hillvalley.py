def hillvalley(l):
    count=0
    for i in range(len(l)-2):
        if l[i] < l[i+1]:
            if l[i+1] < l[i+2]:
                continue
            else:
                count+=1
        else:
            if l[i+1] > l[i+2]:
                continue
            else:
                count+=1
    if count==1:
        return True
    else:
        return False
    
result=hillvalley([1,2,3,4,5])
print(result)