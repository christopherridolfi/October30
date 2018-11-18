import random

result = []

times = int(input("How Many Times Does Player 1 To Roll The Dice"))

for x in range(0,times):
    number = random.randint(1,6)
    result.append(number)
print("Player 1 Roll History is ")
print(result)


result2 = []

times2 = int(input("How Many Times Does Player 2 Want To Roll The Dice"))

for x in range(0,times2):
    number2 = random.randint(1,6)
    result2.append(number2)
print("Player 2 Roll History is ")
print(result2)


result3 = []

times3 = int(input("How Many Times Does Player 3 Want To Roll The Dice"))

for x in range(0,times3):
    number3 = random.randint(1,6)
    result3.append(number3)
print("Player 3 Roll History is ")
print(result3)


result4 = []

times4 = int(input("How Many Times Does Player 4 Want To Roll his Dice"))

for x in range(0,times4):
    number4 = random.randint(1,6)
    result4.append(number4)
print("Player 4 Roll History is ")
print(result4)