# empty_dict = {}

# while True:
#     try:
#         # Accessing a non-existent key in the dictionary
#         value = empty_dict['test_case']
#     except KeyError as e:
#         # Reveal the key used in the test case input
#         print(f"Test case revealed: {e}")
#         break


def access_empty_dict(test_cases):
    """Accesses an empty dictionary using test cases as keys and reveals them as exceptions.

    Args:
        test_cases: A list of test case inputs.
    """

    empty_dict = {}
    for test_case in test_cases:
        try:
            value = empty_dict[test_case]
            print(f"Test case {test_case} accessed successfully.")
        except KeyError:
            print(f"Test case {test_case} not found in the dictionary.")

# Example usage
test_cases = [1, "hello", 3.14, "world"]
access_empty_dict(test_cases)