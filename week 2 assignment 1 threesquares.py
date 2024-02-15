def threesquares(m):
    if(m<=0):
        return False
    for i in range(m):
        for j in range(m):
            c=(4**i)*((8*j)+7)
            if(c==m):
                return False
    return True

result=threesquares(188)
print(result)