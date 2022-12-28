set_a={1,2,3,44,56,7,9}
set_a.add(7)
set_a.update([2,8])
print(set_a)

set_a.discard(9)

print(set_a)
set_a.clear()

set_a = {1,2,4,6,7}
set_b = {3,5,8,9,7}
diff = set_a ^ set_b
print(diff)

set_1={1,2,4,5,6}
set_2={2,4,5}
is_subset=set_2.issubset(set_a)
print(is_subset)

is_superset = set_a.issuperset(set_b)
print(is_superset)

list_a=[1,2,3,3,4,5]
set_a=set(list_a)
print(set_a)


a=[1,2,3,4,5]
b=[3,5]
c=set(a)
d=set(b)
e=c - d
print(e)

l=[]
s=list(map(str,input().split()))
for i in s:
    if i.isdigit():
        l.append(i)
        print(l)



list_a=input()
list_b=[]
for i in list_a:
    if i.isdigit()==True:
         list_b.append(i)
    print(list_b)



li_a=list(map(int,input().split()))
a=len(li_a)
add=int(input())
for i in range(a):
    for j in range(i+1,a):
        if li_a[i]+li_a[j]==add:
print(li_a[i],li_a[j])

