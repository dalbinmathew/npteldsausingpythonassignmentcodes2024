def combinations(d,current=[],sumto=7,test=None):
    if test is None:
        test=[]
    if sum(current)==sumto:
        test.append(current)
    else:
        for i in d:
            if sum(current+[i]) <= sumto:
                combinations(d[i+1:],current+[i],sumto,test)
    return len(test)

print("number of combinations:")
print(combinations([2,3,4]))