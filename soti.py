def find_combinations(numbers, target):
    def backtrack(start, target, path):
        if target == 0:
            result.append(path[:])
            return
        for i in range(start, len(numbers)):
            if numbers[i] <= target:
                path.append(numbers[i])
                backtrack(i, target - numbers[i], path)
                path.pop()

    result = []
    backtrack(0, target, [])
    return result

numbers = [1, 2, 3, 6, 7]
target = 4
combinations = find_combinations(numbers, target)
print(combinations)
