def breakingRecords(scores):
    # Write your code here
    lower_count = 0
    higher_count = 0
    high_rec_breaker = scores[0]
    low_rec_breaker = scores[0]
    for i in range(len(scores)):
        if high_rec_breaker < scores[i]:
            high_rec_breaker = scores[i]
            higher_count += 1
        elif low_rec_breaker > scores[i]:
            low_rec_breaker = scores[i]
            lower_count += 1

    return higher_count, lower_count


print(breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1]))
print(breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]))
