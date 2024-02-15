def sumsquare(l):
    sum=[]
    evensum=0
    oddsum=0
    for i in l:
        if i%2==0:
            evensum += i*i
        else:
            oddsum += i*i
    sum.append(oddsum)
    sum.append(evensum)
    return sum

result=sumsquare([-1,-2,3,7])
print(result)