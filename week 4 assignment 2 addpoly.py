def addpoly(p1,p2):
    sumlist=[]
    for i in p1:
        x=i[1]
        if ispresentinsumlist(sumlist,x):
            continue
        else:
            if ispresent(p2,x):
                exp=()
                soc=i[0]+ispresent(p2,x)
                exp+=(soc,x)
                sumlist.append(exp)
            else:
                exp=()
                exp+=(i[0],x)
                sumlist.append(exp)
    
    for i in p2:
        x=i[1]
        if ispresentinsumlist(sumlist,x):
            continue
        else:
            exp=()
            exp+=(i[0],x)
            sumlist.append(exp)
                
    for i in sumlist:
        if i[0]==0:
            sumlist.remove(i)
    z=sorted(sumlist)
    return z
            
def ispresentinsumlist(sumlist,x):
    for i in sumlist:
        if i[1]==x:
            return True 
       

def ispresent(p,n):
    for i in p:
        s=i[1]
        if s==n:
            y=i[0]
            return y

                    
result=addpoly([(4,3),(3,0)],[(-4,3),(2,1)])
print(result)