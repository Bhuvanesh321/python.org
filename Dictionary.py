dict_a={"name": "nag","rollno": 9}
print(dict_a)
dict_a.update({"name":"gan"})
print(dict_a)
dict_a.update({"rollno":10})
print(dict_a)
keys_list=list(dict_a.keys())
print(keys_list)

dict_a={"name":"jaarumitaya","age":20}
print(dict_a)
msg="huii {}. your age {} right."
print(msg.format("oreo", 2))

dict_a={"name":"jaarumitaya","age":20}
print(dict_a)
del dict_a["name"]
print(dict_a)

li_a=["P","y","t","h","o","n"]
c=int(input())
for i in range (c):
    t=li_a[0]
    li_a.remove(t)
    li_a.append(t)
    print(li_a)









