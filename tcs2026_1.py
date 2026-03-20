import sys

data = sys.stdin.read().split()
idx = 0

L = int(data[idx])
idx += 1
R = int(data[idx])
idx += 1

result = []

for num in range(L, R + 1):
    if num % 7 != 0:
        continue
    if num % 5 == 0:
        continue
    
    s = str(num)
    
    # Check palindrome
    if s == s[::-1]:
        continue
    
    # Check all digits unique (no repeat)
    if len(s) != len(set(s)):
        continue
    
    result.append(str(num))

if result:
    print(' '.join(result))
else:
    print(-1)
    
    
#input
# 1 100
# ^Z
# output:
# 14 21 28 42 49 56 63 84 91 98   