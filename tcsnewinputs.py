# import sys
# data = sys.stdin.read().split()
# i = 0

#--------------------------------------------------------------------------------------------------


# 8️⃣ Weird repeated input (VERY COMMON IN TCS ⚠️)
# Input:
# 2 3
# 2 3
# 2 3
# 2 3

# 👉 Actual meaning:
# First 2 3 → parameters (say s, n)
# Next lines → data repeated n times


# code:
# s = int(data[i]); i += 1
# n = int(data[i]); i += 1

# matrix = []
# for _ in range(n):
#     row = list(map(int, data[i:i+s]))
#     i += s
#     matrix.append(row)

# print(matrix)


# #input:
# 2 3
# 2 3
# 2 3
# 2 3
# ^Z
# #output:
# [(2, 3), (2, 3), (2, 3)]


# 4 2
# 1 2 3 4
# 5 6 7 855
# ^Z
# [[1, 2, 3, 4], [5, 6, 7, 855]]


#--------------------------------------------------------------------------------------------------



# 9️⃣ Continuous numbers (no structure)
# Input:
# 1 2 3 4 5 6 7

# Code:
# arr = list(map(int, data))
# print(arr)


# input and output:
# 1 2 3 4 5 6 7
# ^Z
# [1, 2, 3, 4, 5, 6, 7]


#--------------------------------------------------------------------------------------------------

# # Single integer
# n = int(input())

# # Two integers same line
# a, b = map(int, input().split())

# # Array of integers same line
# arr = list(map(int, input().split()))

# # String
# s = input().strip()
# print(s)

# # Comma-separated (rare but asked sometimes)
# nums = list(map(int, input().split(',')))
# print(nums)

#--------------------------------------------------------------------------------------------------

# 2. Very Safe & Cleaner (Recommended #2 – Especially for matrix/known lines)
                        
# import sys
# input = sys.stdin.readline   # overrides built-in input() to make it faster

# N, M = map(int, input().split())
# matrix = []
# for i in range(M):
#     row = list(map(int, input().split()))
#     matrix.append(row)
# print(matrix)

# # input and output:
# # 2 3
# # 2 3
# # 2 3
# # 2 3
# # [[2, 3], [2, 3], [2, 3]]

# 2 3
# 100 200 300 400
# 10
# 7  
# [[100, 200, 300, 400], [10], [7]]


#--------------------------------------------------------------------------------------------------