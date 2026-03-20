import sys
input = sys.stdin.readline   # overrides built-in input() to make it faster

N, M = map(int, input().split())
matrix = []
for i in range(M):
    row = list(map(int, input().split()))
    matrix.append(row)
print(matrix)