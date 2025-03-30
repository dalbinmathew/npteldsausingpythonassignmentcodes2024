from collections import Counter

def process_string(s):
    if not s:
        print("Invalid Input")
        return
    
    # Count frequencies and track first occurrences
    freq = Counter(s)
    first_occurrence = {}
    for i, char in enumerate(s):
        if char not in first_occurrence:
            first_occurrence[char] = i

    # Find first non-repeating character
    first_non_repeating = None
    for char in s:
        if freq[char] == 1:
            first_non_repeating = char
            break
    
    # Find most frequent character
    max_frequency = max(freq.values())
    most_frequent_chars = [char for char, count in freq.items() if count == max_frequency]
    most_frequent_char = min(most_frequent_chars, key=lambda x: first_occurrence[x])

    # Output results
    if first_non_repeating:
        print(f"First non-repeating character: {first_non_repeating}")
    else:
        first_repeating = min((char for char in s if freq[char] > 1), key=lambda x: first_occurrence[x])
        print(f"None, First Repeating Character: {first_repeating}")

    print(f"Most Frequent Character: {most_frequent_char} (Frequency: {max_frequency})")

# Example Usage
process_string("aabbcc")
