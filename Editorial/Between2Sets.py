def gcd(a, b):
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


def lcm(a, b):
    return (a / gcd(a, b)) * b


# print(lcm(18, 12))

def getTotalX(a, b):
    multiple = 0
    for i in b:
        multiple = gcd(multiple, i)

    factor = 1
    for i in a:
        factor = lcm(factor, i)
        if factor > multiple:
            return 0

    if multiple % factor != 0:
        return 0

    # value = multiple / factor
    # maximum = max(factor, value)

    totalx = 1

    i = factor
    while i < multiple:
        if multiple % i == 0 and i % factor == 0:
            totalx += 1
        i += 1

    return totalx


print(getTotalX([2, 4], [16, 32, 96]))
