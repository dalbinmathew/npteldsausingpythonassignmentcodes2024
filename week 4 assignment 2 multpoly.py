def multpoly(p1,p2):
    multlist=[]
    for i in p1:
        for j in p2:
            elelist=[]
            m=i[0]*j[0]
            n=i[1]+j[1]
            elelist.append(m)
            elelist.append(n)
            multlist.append(elelist)  
        
    for i in range(len(multlist)):
        for j in range(i+1,len(multlist)):
            if multlist[i][1]==multlist[j][1]:
                multlist[i][0]+=multlist[j][0]
                multlist.remove(multlist[j])
                break
            
    i = len(multlist) - 1
    while i >= 0:
        if multlist[i][0] == 0:
            multlist.pop(i)
        i -= 1

    oplist=[]
    for i in multlist:
        i=tuple(i)
        oplist.append(i)
        
    return(oplist)

result=multpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)])
print(result)