def transpose(m):
    t=[]
    temp=[]
    for i in range(len(m[0])):
        for j in range(len(m)):
            t1=m[j][i]
            temp.append(t1)
        t.append(temp)
        temp=[]
    return t

result=transpose([[1,2,3],[4,5,6]])
print(result)