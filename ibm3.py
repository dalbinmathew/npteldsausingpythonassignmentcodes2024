# Write a program to find HCF of two numbers by without using recursion.


def hcf(num1,num2):
    if num1 ==1 or num2==1:
        return 1
    if num1==0 or num2==0:
        return max(num1,num2)
    if num1<0:
        num1*=-1
    if num2<0:
        num2*=-1
    lst=[]
    for i in range (2,min(num1,num2)+1):
        if num1%i==0 and num2%i==0:
            lst.append(i)
    if not lst:
        return None        
    return lst[-1]


n1,n2=-3,5
print(hcf(n1,n2))