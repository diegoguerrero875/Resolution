def birthday(s, d, m):
    # s list of numbers
    # d total of the sum
    # m number of tiles (s)
    c = 0
    lastindex = len(s) - m 
    for i in range(lastindex + 1):
        arr = s[i:i + m]
        if sum(arr) == d:
            c += 1
        
    return c

