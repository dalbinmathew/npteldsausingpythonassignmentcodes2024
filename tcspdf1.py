# Given a maximum of four digits to the base 17(10 -> A, 11 -> B, 12 -> C, 16 -> G) as
# input, output its decimal value.
# input=23GF
# output=10980

num=str(input())
print(int(num,17))