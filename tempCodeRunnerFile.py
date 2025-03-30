from collections import OrderedDict
lst=[]
lst2=[1,4,2,3,4]
lst.append(lst2[:])
y=list(OrderedDict.fromkeys(lst2))
x = "".join(str(item) for item in lst2)
z= "".join(map(str, lst2))
print (x,z)