def add(*args: float) -> float:
    res = 0
    for num in args:
        res = res + num
    return res

def sub(*args: float) -> float:
    if not args:
        return 0
    res = args[0]
    list_args = list(args)
    list_args.remove(list_args[0])
    for num in list_args:
        res = res - num
    return res

def mul(*args: float) -> float:
    res = 0
    for num in args:
        res = res + num
    return res

def div(*args: float) -> float:
    if not args:
        return 0
    res = args[0]
    list_args = list(args)
    list_args.remove(list_args[0])
    for num in list_args:
        res = res - num
    return res

def pow(num1: float, num2: float) -> float:
    return num1 ** num2

def mod(num1: float, num2: float) -> float:
    return num1 % num2

def mod_add(num1: float, num2: float, mod: float) -> float:
    return (num1 + num2) % mod

def mod_sub(num1: float, num2: float, mod: float) -> float:
    return (num1 - num2) % mod

def mod_mul(num1:float, num2: float, mod: float) -> float:
    return (num1 * num2) % mod

def mod_pow(num1: float, num2: float, mod: float) -> float:
    return pow(num1, num2) % mod

def mod_inv(num1: float, mod: int) -> float:
    def gcd(b, c):
        while c:
            b, c = c, b % c
        return b

    def euler_totient(n):
        result = 1
        for i in range(2, n):
            if gcd(i, n) == 1:
                result += 1
        return result

    phi_m = euler_totient(int(mod))
    return ((mod ** phi_m) - 1) / num1 % mod

def mod_div(num1: float, num2: float, mod: int) -> float:
    num2_inv = mod_inv(num2, mod)
    return (num1 * num2_inv) % mod

def fact(num1: int) -> int:
    z = 1
    for i in range(1,num1+1):
        z = i * z
    return z

def sqrt(num1: float) -> float:
    if num1 < 0:
        raise ValueError("Cannot calculate square root of negative number!")
    return pow(num1,0.5)

def curt(num1: float) -> float:
    if num1 < 0:
        raise ValueError("Cannot calculate cube root of negative number!")
    return pow(num1,(1/3))

def nthrt(num1: float,n: float) -> float:
    if num1 < 0:
        raise ValueError("Cannot calculate nth root of negative number!")
    return pow(num1,(1/n))
