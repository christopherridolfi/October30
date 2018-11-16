j= 0
t=0
shoppinglist = []

def shopping():
    x = 0
    while x == 0:
        end_list = input("Do you want to end the shopping list?")
        if end_list == "yes":
            x = x + 1
            print(shoppinglist)
            return shoppinglist
        else:
            y = 1
            while y == 1:
                list = input("What do you want to add to the shopping List?")
                shoppinglist.append(list)
                y = 2


shopping()



row_1 = [1,2,3]
row_2 = [4,5,6]
row_3 = [7,8,9]

tic_tac = [row_1, row_2,row_3]
 #First num is row, second is columb
while j == 0:
    start = input("Wanna Play Your Move in TIC TAC TOE")
    if start == "no":
        print("GAME OVER")
        j=1
    else:
        while t == 0:
            place = input("Where Do you Want To Place Your X (tr = Top Right) (br = Bottom Right) (mm = Middle Middle")
            for x in tic_tac:
                print(x)

            if place == "tr":
                tic_tac[0][2] = 0
            elif place == "br":
                tic_tac[2][2] = 0
            elif place == "bl":
                tic_tac[2][0] = 0
            elif place == "bm":
                tic_tac[2][1] = 0
            elif place == "tm":
                tic_tac[0][1] = 0
            elif place == "tl":
                tic_tac[0][0] = 0
            elif place == "mr":
                tic_tac[1][2] = 0
            elif place == "mm":
                tic_tac[1][1] = 0
            elif place == "ml":
                tic_tac[1][0] = 0
            if tic_tac[0][0] + tic_tac[0][2] + tic_tac[0][1] == 0:
                print("You Win")
                t = t+1
            if tic_tac[1][0] + tic_tac[1][1] + tic_tac[1][2] == 0:
                print("You Win")
                t = t+1
            if tic_tac[2][2] + tic_tac[2][0] + tic_tac[2][1] == 0:
                print("You Win")
                t = t+1
            if tic_tac[2][0] + tic_tac[1][1] + tic_tac[0][2] == 0:
                print("You Win")
                t = t+1
            if tic_tac[2][2] + tic_tac[1][2] + tic_tac[0][2] == 0:
                print("You Win")
                t = t+1
            if tic_tac[2][1] + tic_tac[1][1] + tic_tac[0][1] == 0:
                print("You Win")
                t = t+1
            if tic_tac[2][0] + tic_tac[1][0] + tic_tac[0][0] == 0:
                print("You Win")
                t = t+1
            if tic_tac[0][0] + tic_tac[1][1] + tic_tac[2][2] ==0:
                print("You Win")
                t = t+1






inlist = [2,5,3,6]

def LargestValue(inlist):
    inlist.sort()
    return inlist[3] # Returns the new value as the function.

print(LargestValue(inlist)) # Calling Up the Function

list1 = [1, 2, 3, 4]  # do max number then all nubmers exept that one then all numbers except that.
list2 = [5, 6, 7, 8, 9, 10]
list3 = list1 + list2
max1 = []
for x in range(len(list3)):
    max1.insert(0, max(list3))
    list3.remove(max(list3))
    print(max1)




