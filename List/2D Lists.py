a = [1,2,3]
b = [99,98,97]
c = [7,8,9]
newlist = [a,b,c]
print(newlist[1][1])

for x in newlist:
    print(x)

string_list = ["hello", "World"]
print(string_list[1][2])




for x in newlist:
    for y in x:
        print(y)