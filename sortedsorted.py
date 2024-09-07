def uncommong(l1,l2):
    l=[]
    for i in l1:
        if i not in l2:
            if i not in l:
                l.append(i)
    for i in l2:
        if i not in l1:
            if i not in l:
                l.append(i)
    return sorted(l)
result=uncommong([2,2,4],[1,3,3,4,5])
print(result)