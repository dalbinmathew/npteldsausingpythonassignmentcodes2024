lst=[2,6,1,5,4]
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]>lst[j]:
            lst[j],lst[i]=lst[i],lst[j]
print(lst)