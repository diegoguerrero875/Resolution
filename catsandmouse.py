#hacker racnk cats and a mouse problem
def catAndMouse(x, y, z):
    if abs(x-z) < abs(y-z):
        a ="Cat A"
    elif abs(y - z) < abs(x - z):
        a ="Cat B"
    elif abs(x - z) == abs(y - z):
        a = "Mouse C"

    return(a)
