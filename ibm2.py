# you just have to return the sum of sums of all the subsets that can be formed from an array

def sosb(nums):
    n=len(nums)
    s = [0]
    for i in range(n):
        v = len(s)
        for t in range(v):
            s.append(s[t] + nums[i])
    return sum(s)


arr=[5,4,3]
print(sosb(arr))