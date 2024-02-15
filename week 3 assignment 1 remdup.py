def remdup(l):
    l2=[]
    for i in range(len(l)):
        if l[i] not in l2:
            l2.append(l[i])
    return l2

result=remdup([3,5,7,5,3,7,10])
print(result)