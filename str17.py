# Program to remove a newline in Python

temp=["\ncat\n","dog\n","cow\n","goat\n"]
new_list=[]
for i in temp:
    new_list.append(i.replace("\n",""))
print("string before :"+"".join(temp))
print("string after :"+" ".join(new_list))
