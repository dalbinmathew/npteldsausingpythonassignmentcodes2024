def combinations(d, current=[], sumto=7, test=None, start=0):
    if test is None:
        test = []  # Initialize test list once when the function is first called
    
    if sum(current) == sumto:
        test.append(current)
    else:
        for i in range(start, len(d)):
            if sum(current + [d[i]]) <= sumto:
                # Avoid reusing the same element by starting at the current index + 1
                combinations(d, current + [d[i]], sumto, test, i + 1)
    
    return len(test)

print("Number of combinations:")
print(combinations([2,3,4], sumto=7))

