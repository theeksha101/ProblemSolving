def divisibleSumPairs(n, k, ar):
    # Write your code here
    count_no_pair = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                count_no_pair += 1

    return count_no_pair
