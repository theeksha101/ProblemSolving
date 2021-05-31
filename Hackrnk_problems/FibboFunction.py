def fibbo(n):
    a, b = 0, 1

    while a < n:
        return a
        result = a
        a = b
        b = result + a
        return b


print(fibbo(20))