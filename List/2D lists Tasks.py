list_1 = ["Hi","Hola","Bonjour"]
list_2 = ["Goodbye", "aur revoir", "Chow"]
list_total = [list_1,list_2]
print(list_total)


def question():
    for x in list_total:
        for y in x:
            print(y)
question()


sumlist1 = [1,2,3]
sumlist2 = [2,4]
sumtotal = [sumlist1,sumlist2]

def duh():
    sum = 0
    for x in sumtotal:
        sum += x[1]
    return sum

print(duh())

def dun():
    sum1 = 0
    for y in sumtotal[0]:
        sum1 += y
    return sum1

print(dun())





