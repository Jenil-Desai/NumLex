def perm(n,k):
    y = 1
    for i in range(1,n+1):
        y = i * y
    z = 1
    for i in range(1,(n-k)+1):
        z = 1 * z
    return (y // z)

def comb(n,k):
    x = 1
    for i in range(1,n+1):
        x = i * x
    y = 1
    for i in range(1,k+1):
        y = i * y
    z = 1
    for i in range(1,(n-k)+1):
        z = 1 * z
    return (x // (y * z))
