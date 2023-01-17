# Solution for Hacker rank Divisible Sum Pairs problem
def divisibleSumPairs(n, k, ar):
    c = 0
    position = range(len(ar))
    for i in position:
        for j in position:
            if i < j and (ar[i] + ar[j]) % k == 0:
                c += 1
                
    return c
