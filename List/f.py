list1 = [1,2,3,4] #do max number then all nubmers exept that one then all numbers except that.
list2 = [5,6,7,8,9,10]
list3 = list1+list2
max1 = []
for x in range(len(list3)):
    max1.insert(0,max(list3))
    list3.remove(max(list3))
    print(max1)





