def f(billamount):
    if billamount < 500:
        return billamount+(0.05*billamount)
    elif billamount >= 500 and billamount < 2500:
        return billamount+(0.1*billamount)
    elif billamount >= 2500:
        return billamount+(0.2*billamount)
billamount=int(input())
print(f(billamount))

