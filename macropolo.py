def f(n):
    if n%3==0:
        print("macro")
    elif n%5==0:
         print("polo")
    elif n%3==0 and n%5==0:
         print("MacroPolo")
    else:
        print("no")
n=int(input())
f(n)

