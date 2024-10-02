# Input :
# 10 -> Integer
# Output :
# 5 -> result- Integer
# Explanation:
# Binary representation of 10 is 1010. After toggling the bits(1010), will get 0101 which represents
# “5”. Hence output will print “5”.

def bs(a):
    test=""
    z=str(bin(a)[2:])
    for i in z:
        if i =="0":
            test+="1"
        else:
            test+="0"
    return int(test,2)

z=bs(10)
print(z)