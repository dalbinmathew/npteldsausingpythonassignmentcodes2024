# N=8 and arr = [4,5,0,1,9,0,5,0].
# There are 3 empty packets in the given set. These 3 empty packets represented as O should be
# pushed towards the end of the array
# Input :
# 8 – Value of N
# [4,5,0,1,9,0,5,0] – Element of arr[O] to arr[N-1],While input each element is separated by newline
# Output:
# 4 5 1 9 5 0 0 0

def pz(N,arr):
    l1=[]
    l2=[]
    for i in arr:
        if i!=0:
            l1.append(i)
        else:
            l2.append(i)
    return l1+l2

op=pz(8,[4,5,0,1,9,0,5,0])
print(op)