def find_valid_pairs(n, x, y, arr):
    count = 0
    pairs = []

    # Iterate through all possible pairs (i, j)
    for i in range(n):
        for j in range(n):
            # Perform string addition
            num_str = str(arr[i]) + str(arr[j])
            num_int = int(num_str)
            
            # Check if the number is within the range
            if x <= num_int <= y:
                count += 1
                pairs.append((arr[i], arr[j]))

    print(f"Total valid pairs: {count}")
    print("Valid pairs:", pairs)

# Example input
n = 5
x = 20
y = 50
arr = [2, 5, 7, 6, 3]

find_valid_pairs(n, x, y, arr)
