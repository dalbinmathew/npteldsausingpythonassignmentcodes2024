list=[1,3,2,4]
print("mean=",sum(list)/len(list))
x=sorted(list)
y=int(len(x)/2)
if len(x)%2==0:
    med=(x[y-1]+x[y])/2
else:  
    med=x[y]
print("median=",med)