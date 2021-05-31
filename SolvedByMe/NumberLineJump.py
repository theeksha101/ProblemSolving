def kangaroo(x1, v1, x2, v2):
    yes = "YES"
    no = "NO"

    for i in range(10000):
        closer_location_k2 = x1 + v1 * i
        closer_location_k1 = x2 + v2 * i
        if closer_location_k2 == closer_location_k1:
            return yes
    else:
        return no


print(kangaroo(0, 2, 5, 3))
