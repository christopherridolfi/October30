import random

list_1 = ["Hi", "Hello", "Hola", "bonjuer", "Chow"]
print(list_1)
del list_1[2]
print(list_1)


list_2 = [random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10), random.randint(0,10), random.randint(0,10)]
print(list_2)
if list_2[0] % 2 == 0:
    print("Even")
else:
    print("Odd")
if list_2[1] % 2 == 0:
    print('Even')
else:
    print("Odd")
if list_2[2] % 2 == 0:
    print("Even")
else:
    print('Odd')
if list_2[3] % 2 == 0:
    print("Even")
else:
    print('Odd')
if list_2[4] % 2 == 0:
    print("Even")
else:
    print("Odd")
if list_2[5] % 2 == 0:
    print("Even")
else:
    print("Odd")


gwood = "Chrizzzz"
for x in gwood:
    print(x)


string = "Hello World"
reverse_string = string[::-1]
print(reverse_string)

sentance = "You're a wizard Harry."


newlist =[]
for s in sentance:
    if s == "e":
        newlist.append("3")
    else:
        newlist.append(s)
newlist
print(newlist)

