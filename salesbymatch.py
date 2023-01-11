#sale by match on HackerRank

def sockMerchant(n, ar):
    # Write your code here
    k = 0
    socks = {}
    for i in ar:
        if i not in socks:
            socks[i] = 1
        else:
            socks[i] += 1

    for e in socks:
        k += socks[e] // 2

    return k
