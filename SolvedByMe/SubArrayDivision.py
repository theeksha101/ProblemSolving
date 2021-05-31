# sharing chocolate
# [    |    |   |   |   |   ]
# each square has number
# Lily decides to share in contiguous segments
# 1. length of the segment matches Ron's birth month
# 2. the sum of the integers on the squares is equal to his birth day.

def birthday(s, d, m):
    # Write your code here

    count = 0
    for i in range(len(s)):
        j = i
        summation = 0
        for k in range(m):
            if j >= len(s):
                break
            summation = summation + s[j]
            j += 1

        if summation == d:
            count += 1

    return count


print(birthday([1, 2, 1, 3, 2], 3, 2))
print(birthday([1, 1, 1, 1, 1, 1], 3, 2))
print(birthday([4], 4, 1))