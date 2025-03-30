# first question is where three strings will be given and we have to make them into a single string merging them in alphabetical order.



# 1 = abc

# 2 = ghi

# 3 = def

# result = abcdefghi


def comb(s1,s2,s3):
    res=""
    l=[]
    l.append(s1)
    l.append(s2)
    l.append(s3)
    x=sorted(l)
    res+=x[0]
    res+=x[1]
    res+=x[2]
    return res

st1="one"
st2="two"
st3="three"
print(comb(st1,st2,st3))