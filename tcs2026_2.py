import sys

data = sys.stdin.read().split()
idx = 0

N = int(data[idx]); idx += 1
M = int(data[idx]); idx += 1

count = 0

for _ in range(N):
    marks = []
    for __ in range(M):
        marks.append(int(data[idx]))
        idx += 1
    
    avg = sum(marks) / M
    if avg > 50:
        count += 1

print(count)