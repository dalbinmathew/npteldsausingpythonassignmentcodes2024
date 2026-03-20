def fibtriangle(lim):
    if lim>0:
        x=1
        y=2
        if lim==1:
            print(1)
        elif lim==2:
            print(1)
            print("1 2")
        else:
            print(1)
            print("1 2")
            for i in range(2,lim):
                lst=[]
                for j in range(i+1):
                    z=x+y
                    lst.append(str(z))
                    x=y
                    y=z
                print(" ".join(lst))
        
limit=5
fibtriangle(limit)
                