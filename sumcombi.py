def combinations(d, current=[], sum_to=7, test=None):
    if test is None:
        test = []  # Initialize test once when the function is first called
    
    if sum(current) == sum_to:
        test.append(current)
    else:
        for i in d:
            if sum(current + [i]) <= sum_to:
                combinations(d, current + [i], sum_to, test)
    
    return test

print(combinations([2,3,4]))
