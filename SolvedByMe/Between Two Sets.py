def findFactor(number):
    i = 1
    list_factors = []
    while i not in list_factors:
        if number % i == 0:
            list_factors.append(int(number / i))
            list_factors.append(i)
            list_factors = list(set(list_factors))
        i += 1
    list_factors.sort()
    return list_factors


def checkFactor(numerator_set, denominator_set):
    factors_set = []

    for i in numerator_set:
        check_factor = []
        for j in denominator_set:
            if i % j != 0:
                check_factor.append(1)
        if len(check_factor) == 0:
            factors_set.append(i)

    return factors_set


def getTotalX(a, b):
    # Write your code here
    combined_factors_set_b = set()
    for ele in b:
        combined_factors_set_b.update(findFactor(ele))

    combined_factors_set_b = list(combined_factors_set_b)
    combined_factors_set_b.sort()

    print(combined_factors_set_b)

    factors_set_a = checkFactor(combined_factors_set_b, a)
    print(factors_set_a)

    count_final_factors = 0

    for i in factors_set_a:
        check_factor = []
        for j in b:
            if j % i != 0:
                check_factor.append(i)
        if len(check_factor) == 0:
            count_final_factors += 1

    return count_final_factors


print(getTotalX([100, 99, 98, 97, 96, 95, 94, 93, 92, 91], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
