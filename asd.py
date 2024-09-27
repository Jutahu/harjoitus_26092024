'''juuuh'''
print("moi juha xdd")

def moro(n):
    if n == 1:
        print("")
        return 1
    else:
        print("moi!", end=" ")
        return moro(n - 1)
def xdd(n2):
    if n2 == 1:
        print("")
        return 1
    else:
        print("x"+"d"*n2, end=" ")
        return xdd(n2 - 1)


moro(3)
xdd(6)