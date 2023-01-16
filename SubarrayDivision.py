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

# another way to solve using list comprehension
def birthday(s, d, m):
    c = sum(sum(s[i:i + m]) == d
            for i in range(len(s) - m + 1))
    return c

#this way the code is reducted to 3 lines
