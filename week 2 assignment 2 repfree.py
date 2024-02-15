def repfree(str):
    l1=[]
    for i in str:
        l1.append(i)
    s1=set(l1)
    if(len(s1)==len(l1)):
        return True
    else:
        return False

result=repfree("(x+6)[y-5]")
print(result)