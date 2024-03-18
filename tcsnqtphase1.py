def strtolist(str):
    x=str.split(" ")
    lst=[]
    test=[]
    test2=[]
    k= 0
    m=0
    for i in x:
        for j in i:
            test.append(j)
    while m <16:
        while k < 4:
            if m >= len(test):
                test2.append("_")
            else:
                test2.append(test[m])
            k +=1
            m+=1
        k=0
        lst.append(test2)
        test2=[]
        
    return lst
    
    
result=strtolist("hello my guys")
print(result)