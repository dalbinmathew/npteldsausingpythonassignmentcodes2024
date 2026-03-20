months = int(input())

# If months <= 0 or invalid
if months <= 0:
    print("Error")
    sys.exit()

# Package durations and their costs
packages = [
    (1, 2000),
    (3, 5000),
    (6, 9000),
    (9, 12000),
    (12, 15000)
]

# DP array: min_cost[i] = minimum cost to cover exactly i months
INF = float('inf')
min_cost = [INF] * (months + 1)
min_cost[0] = 0  # 0 months costs 0

for i in range(1, months + 1):
    for duration, cost in packages:
        if duration <= i and min_cost[i - duration] != INF:
            min_cost[i] = min(min_cost[i], min_cost[i - duration] + cost)

if min_cost[months] == INF:
    print("Error")
else:
    print(min_cost[months])