def orangecap(d):
    t=()
    d2={}
    for i in d.values():
        for j,k in i.items():
            if j not in d2:
                d2[j]=k
            else:
                d2[j]+=k
    x=d2.values()
    maxtotalscore=max(x)
    for j,k in d2.items():
        if k==maxtotalscore:
            t+=(j,)
            t+=(k,)
            break
    return t

result=orangecap({'test1':{'Pant':84, 'Kohli':120}, 'test2':{'Pant':59, 'Gill':42}})
print(result)