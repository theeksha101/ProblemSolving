if __name__ == '__main__':
    x = 1
    y = 1
    z = 2
    n = 3
    possible_combination = []

    for i in range(0, x + 1):
        for j in range(0, y + 1):
            for k in range(0, z + 1):
                possible_combination.append([i, j, k])

    not_sum_to_n = []
    for i in possible_combination:
        if sum(i) != n:
            not_sum_to_n.append(i)

    print(possible_combination)
    print(not_sum_to_n)