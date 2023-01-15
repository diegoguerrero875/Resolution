#apple and orange problem from hacker rank
def countApplesAndOranges(s, t, a, b, apples, oranges):
    c1 = 0
    c2 = 0
    for i in apples:
        if a + i in range(s,t+1):
            c1 += 1
    for i in oranges:
        if b + i in range(s,t+1):
            c2 += 1
    
    print(c1)
    print(c2)
