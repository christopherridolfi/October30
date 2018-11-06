list_1 = ["Hello", "My", "Name", "Is", "Octocat", "MEOW"]
for x in list_1:
    print(x)

change = ["H", "E", "L", "L", "O"]
for t in change:
    print(t)
change[0] = "U"
change[1] = "S"
change[2] = "U"
change[3] = "C"
change[4] = "K"
for g in change:
    print(g)


ten_num = [1,3,2,4,6,5,7,9,8,10]
print(ten_num)
ten_num.sort()
print(ten_num)

list_one = [1,2,6,7,9,11]
print(list_one)
list_two = [1,3,6,8,99]
print(list_two)

highest_value = list_one + list_two
highest_value = max(highest_value)
print(highest_value)


out_list = [1,2,5,6,7,8,8,8,9,9,9,9,0,1,2,4]
for out in out_list:
    print(out)

value = [0,1,2,3,4,5,6,7,8,9,10]
for other in value:
    print(other[2])