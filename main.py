print("hello")# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
a={1,2,3,4}
print(type(a))
a={10+20}
   print(a)

 print("python is amazing ")

a=("bhu")
b=("vi")
c=(a+b)
print(len(c))

a=10
b=20
print(
    \a/b)
print(a%b)



 list_a = [1,2]
 list_b = list_a
 list_a = list_a+[6,7]

 print(str(list_a))
 print(str(list_b))

 numbers = "1  2 3 4"
 num_list = numbers.split(" ")
 print(num_list);



 string_a="python is astronishing"
 list_a=string_a.split('a')
 print(list_a)

 list_a=[5,4,3,2,1]
 list_b =list_a[::-1]
 print(list_b)

m=1
n=5
m=str(m)
a=m*n
print(a)

a=int(input("enter the value"))
b=int(input("enter the value"))
c=list()
c.append(a)
n=b*c
print(n)

a="Apple"
b="Application"
if(a[:3] == b[:3]):
    print("same")
else:
    print("Not same")

    a = '123'
    b = '432'
    if a[0] < b[2]:
        print("first digit of a is less than last digit of b")
    else:
        print("first digit of a is greater than last digit of b")

    l = '123'
    h = '456'
    print(l[0] < h[2])

m=70
p=40
c=40
if(m>=70 or p>=60 or c>=60 or m+p+c>=180):
    print("satisfied")
else:
    print("not satisfied")

a="waterfall"
part= a[0:7:2]
print(part)

a="MAhesh"
b=a[0:5:1]
print(b)

n=".Mowa"
n=n.strip(".")
print(n)

n = "PyThOn"
v = n.swapcase()
print(v)

n="dd-mm-yy"
print(n.replace("-" , "/"))

a="malayalam"
x= a[::-1]
if(a==x):
    print("palindrome")
else:
    print("not palindrome")

n=input()
print(n[-1])
