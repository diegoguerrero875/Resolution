# Bill Division from Hacker Rank

def bonAppetit(bill, k, b):
    c = sum(bill)/2
    anna = (sum(bill) - bill[k])/2
    if anna == b:
        print("Bon Appetit")
    else:
        print(int(b - anna))
