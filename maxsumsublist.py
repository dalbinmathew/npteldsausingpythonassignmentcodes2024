# Write function mssl() (minimum sum sublist) that takes as 
# input a list of integers. It then computes and returns the 
# sum of the maximum sum sublist of the input list. The maximum sum 
# sublist is a sublist (slice) of the input list whose sum of 
# entries is largest. The empty sublist is defined to have sum 0. 
# For example, the maximum sum sublist of the list 
# [4, -2, -8, 5, -2, 7, 7, 2, -6, 5] is [5, -2, 7, 7, 2] 
# and the sum of its entries is 19.

def mssl(l):
    if l==[]:
        return 0
    mydict={}
    x=[]
    y=0
    for i in range (len(l)):
        for j in range (i+1,len(l)+1):
            x=l[i:j]
            y=sum(x)
            mydict[y]=x
            x=[]
            y=0
    z=sorted(mydict)
    return z[-1]

m=mssl([-2,-3,-5])
print(m)
            