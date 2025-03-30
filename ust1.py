import math
def maxlcm(a):
    maxi=0
    for i in range (len(a)-1):
        x=abs(a[i]*a[i+1])//math.gcd(a[i],a[i+1])
        maxi=max(maxi,x)
    return maxi

arr=[1,2,3,4]
print(maxlcm(arr))