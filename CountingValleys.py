#Hakcer rank counting valleys problem (very slow but runs)
def countingValleys(steps, path):
    c = 0
    r = 0
    bandera = True
    for i in path:
        if i == "U":
            c += 1
        elif i == "D":
            c -= 1
        if c < 0 and bandera:
            r += 1
        if c < 0:
            bandera = False
        elif c == 0:
            bandera = True
    
    return r
