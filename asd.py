'''juuuh'''
print("moi juha xdd")

def moro(n):
    if n == 1:
        print("")
        return 1
    else:
        print("moi!", end=" ")
        return moro(n - 1)


moro(3)