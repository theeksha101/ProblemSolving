def migratoryBirds(arr):
    # Write your code here
    set_arr = set(arr)
    type_frequency = {}

    for i in set_arr:
        type_frequency[i] = arr.count(i)

    most_sighted_type = []

    for key in type_frequency:
        if type_frequency[key] == max(type_frequency.values()):
            most_sighted_type.append(key)

    return min(most_sighted_type)


print(migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]))
