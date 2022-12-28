l="pop up"
l1=list(l)
le=len(l1)
l2=[]
for i in range(le):
    c=l1.count(l1[i])
    if l1[i] !=" " and l1[i] not in l2:
        print(l1[i]," ",c)
        l2.append(l1[i])

n1=tuple(map(int,input().split(" "))
n2=tuple(map(int,input().split(" ")))
list





