# Program to Change Decimal Number to Binary and vice versa

decimal_num = 34
binary_str = bin(decimal_num)
print(binary_str)
binary_str_no_prefix = bin(decimal_num)[2:]
print(binary_str_no_prefix)
# Output: 0b100010


binary_num=100010
print(int(str(binary_num),2))