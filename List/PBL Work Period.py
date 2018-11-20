#Question 6
import random
j= 0
t=0
shoppinglist = []

def shopping():
    x = 0
    while x == 0:
        end_list = input("Do you want to end the shopping list?")
        if end_list == "yes":   #This is an if statement that if answered yes ends the while statement and stops the shopping list problem.
            x = x + 1
            print(shoppinglist)
            return shoppinglist
        else:
            y = 1
            while y == 1:
                list = input("What do you want to add to the shopping List?")
                shoppinglist.append(list)  #This adds the input above to the shopping list.
                y = 2


shopping()

#Question 13

row_1 = [0,0,0]
row_2 = [0,0,0]  #this is a 2d list. This will be used as the Tic Tac Toe Grid.
row_3 = [0,0,0]

tic_tac = [row_1, row_2,row_3]
 #First num is row, second is columb
while j == 0:
    start = input("Wanna Play Your Move in TIC TAC TOE")
    if start == "no":
        print("GAME OVER")
        j=1  #This ends the while statement and therefor ends the peice of code, if You don't wanna play the game.
    else:
        while t == 0:
            for x in tic_tac:
                print(x)  #This prints the 2d list so it gives a visual representation of what the game looks like. It updates when the player moves.
            place = input("Where Do you Want To Place Your X (tr = Top Right) (br = Bottom Right) (mm = Middle Middle")
            player2 = input("Where Does player 2 to want to place X")


            if place == "tr": #This clump of code uses an input to make changes to a specific value from the 2d grid. They change the value depending on what position was typed in in the input peice of code above.
                tic_tac[0][2] = 1
            elif place == "br":
                tic_tac[2][2] = 1
            elif place == "bl":
                tic_tac[2][0] = 1
            elif place == "bm":
                tic_tac[2][1] = 1
            elif place == "tm":
                tic_tac[0][1] = 1
            elif place == "tl":
                tic_tac[0][0] = 1
            elif place == "mr":
                tic_tac[1][2] = 1
            elif place == "mm":
                tic_tac[1][1] = 1
            elif place == "ml":
                tic_tac[1][0] = 1
            if tic_tac[0][0] + tic_tac[0][2] + tic_tac[0][1] == 3: #This is clump of code uses if statement which activate a YOU WIN message when three values added together equal the number in the if statement. This is here so that when three moves from the same player in a row are activated then they win.
                print("Player 1 Win")
                t = t+1
            if tic_tac[1][0] + tic_tac[1][1] + tic_tac[1][2] == 3: #The Various if statements are all the different posibilites for Winning the Game.
                print("Player 1 Win")
                t = t+1
            if tic_tac[2][2] + tic_tac[2][0] + tic_tac[2][1] == 3:
                print("Player 1 Win")
                t = t+1
            if tic_tac[2][0] + tic_tac[1][1] + tic_tac[0][2] == 3:
                print("Player 1 Win")
                t = t+1
            if tic_tac[2][2] + tic_tac[1][2] + tic_tac[0][2] == 3:
                print("Player 1 Win")
                t = t+1
            if tic_tac[2][1] + tic_tac[1][1] + tic_tac[0][1] == 3:
                print("Player 1 Win")
                t = t+1
            if tic_tac[2][0] + tic_tac[1][0] + tic_tac[0][0] == 3:
                print("Player 1 Win")
                t = t+1
            if tic_tac[0][0] + tic_tac[1][1] + tic_tac[2][2] ==3:
                print("Player 1 Win")
                t = t+1

            if player2 == "tr":
                tic_tac[0][2] = 2.1  #This is basicaly a duplicate code from above but there is a 2.1 instead of a 3. This is done becasue there are 2 different players and we must show 2 different values.
            elif player2 == "br":
                tic_tac[2][2] = 2.1
            elif player2 == "bl":
                tic_tac[2][0] = 2.1
            elif player2 == "bm":
                tic_tac[2][1] = 2.1
            elif player2 == "tm":
                tic_tac[0][1] = 2.1
            elif player2 == "tl":
                tic_tac[0][0] = 2.1
            elif player2 == "mr":
                tic_tac[1][2] = 2.1
            elif player2 == "mm":
                tic_tac[1][1] = 2.1
            elif player2 == "ml":
                tic_tac[1][0] = 2.1
            if tic_tac[0][0] + tic_tac[0][2] + tic_tac[0][1] == 6.3: #This is identical code to the if statements above but for player 2 instead of 1.
                print("Player 2 Wins")
                t = t+1
            if tic_tac[1][0] + tic_tac[1][1] + tic_tac[1][2] == 6.3:
                print("Player 2 Wins")
                t = t+1
            if tic_tac[2][2] + tic_tac[2][0] + tic_tac[2][1] == 6.3:
                print("Player 2 Wins")
                t = t+1
            if tic_tac[2][0] + tic_tac[1][1] + tic_tac[0][2] == 6.3:
                print("Player 2 Wins")
                t = t+1
            if tic_tac[2][2] + tic_tac[1][2] + tic_tac[0][2] == 6.3:
                print("You Win")
                t = t+1
            if tic_tac[2][1] + tic_tac[1][1] + tic_tac[0][1] == 6.3:
                print("Player 2 Wins")
                t = t+1
            if tic_tac[2][0] + tic_tac[1][0] + tic_tac[0][0] == 6.3:
                print("Player 2 Wins")
                t = t+1
            if tic_tac[0][0] + tic_tac[1][1] + tic_tac[2][2] ==6.3:
                print("Player 2 Wins")
                t = t+1




#Question 10

inlist = [2,5,3,6]

def LargestValue(inlist):
    inlist.sort() #This peice of code sorts the list from least to highest number.
    return inlist.pop() # Returns the last number in the list. (The Highest Number)

print(LargestValue(inlist)) # Calling Up the Function

#Question 11

def Maxnumber():
    list1 = [1, 2, 3, 4]
    list2 = [5, 6, 7, 8, 9, 10]
    list3 = list1 + list2 #This list is a combination of values from list1 and list2.
    max1 = []
    for c in range(len(list3)): #this function finds the max number puts it in a new list then deltes it fro orignial list. The values are then appended in order.
        max1.insert(0, max(list3))
        list3.remove(max(list3))
    print(max1)

Maxnumber()

#Question 9
innlistt = [2,7,3,4,9]
def pivotlist(innlistt,number):
    newwlist = []
    for x in innlistt:
        if x < number: #This peice of code adds x value to the list if the value is less then the number value.
            newwlist.append(x)
    return newwlist

print(pivotlist(innlistt,6))


#Question 8
results = []
results2 = []
results3 = [] #These are the six lists that will be used in this question. They are empty so I can append them later.
results4 = []
results5 = []
results6 = []

times = int(input("How Many Times Do You Want To Roll The Dice"))

for x in range(0,times):
    numbers = random.randint(1,6)
    if numbers == 1:
        results.append(numbers) #These If statements adds the random radient to one of 6 lists. If the number matches the specific number listed then it will be added to a specific. List. This is done so each specific number is added to a specific list.
    elif numbers == 2:
        results2.append(numbers)#This process will create a list for each side of the dice. And therefor will be used to find how many of each number are there.
    elif numbers == 3:
        results3.append(numbers)
    elif numbers == 4:
        results4.append(numbers)
    elif numbers == 5:
        results5.append(numbers)
    elif numbers == 6:
        results6.append(numbers)

print("Number of 1:")
print(len(results)) #this finds the amount of the same number in the specified list by finding the length.
print("Number of 2:")
print(len(results2))
print("Number of 3:")
print(len(results3))
print("Number of 4:")
print(len(results4))
print("Number of 5:")
print(len(results5))
print("Number of 6:")
print(len(results6))

#Question 12

result = []

times = int(input("How Many Times Does Player 1 To Roll The Dice"))

for x in range(0,times): #This range statement runs through the list from 0 to the input.
    number = random.randint(1,6)
    result.append(number)
print("Player 1 Roll History is ")
print(result)  #The Range allows a history to be formed.



result2 = []

times2 = int(input("How Many Times Does Player 2 Want To Roll The Dice")) #This is a copy of the peice of code above. But the variables are changed for player 2.

for x in range(0,times2):
    number2 = random.randint(1,6)
    result2.append(number2)
print("Player 2 Roll History is ")
print(result2)


result3 = []

times3 = int(input("How Many Times Does Player 3 Want To Roll The Dice")) #Same code as above. But for different Player.

for x in range(0,times3):
    number3 = random.randint(1,6)
    result3.append(number3)
print("Player 3 Roll History is ")
print(result3)


result4 = []

times4 = int(input("How Many Times Does Player 4 Want To Roll his Dice"))  #Same code as above. But for different Player.

for x in range(0,times4):
    number4 = random.randint(1,6)
    result4.append(number4)
print("Player 4 Roll History is ")
print(result4)


