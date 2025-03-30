def longest_palindromic_substring(s):
    def expand_around_center(left, right):
        # Expand as long as the characters on both sides are equal
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return the length of the palindrome
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        # Check for odd-length palindromes (single character center)
        palindrome1 = expand_around_center(i, i)
        # Check for even-length palindromes (two-character center)
        palindrome2 = expand_around_center(i, i + 1)

        # Update the longest palindrome
        if len(palindrome1) > len(longest):
            longest = palindrome1
        if len(palindrome2) > len(longest):
            longest = palindrome2

    return longest

# Example usage
string = "abba"
print(longest_palindromic_substring(string))  # Output: "bab" or "aba"
