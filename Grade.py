import random
def hello_world():
    print("Hello World")


hello_world()



def addition(a, b):
    return a + b

print(addition(3,4))


def multiply(c,d):
    return c * d
print(multiply(2,4))


def grade_percent(value):
    letter = ""

    if value < 50 and value > 0:
        print("F")
    elif value >= 52 and value <= 69:
        print("D")
    elif value >= 70 and value <= 79:
        print("C")
    elif value >= 80 and value <= 89:
        print("B")
    elif value >= 90 and value <= 100:
        letter = "A"
    if value < 0:
        print("Invalid Input")

    return letter


print(grade_percent(int(input("What is your Grade"))))

def doubleeven(n):
    if (n % 2) == 0:
        return n * 2
    if (n % 2) == 1:
        return n

print(doubleeven(int(input("Input a number"))))



def largestNum(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    if num2>num3 and num2>num1:
        return num2
    if num3>num2 and num3>num1:
        return num3

print(largestNum(int(input("Gimme a number")),int(input("Gimme a number")),int(input("Gimme a number"))))




def sumDice(Dice,numRoll):
    sum = 0
    for x in range(1,numRoll):
       sum = sum + random.randint(1,Dice)
    return sum
print(sumDice(4,random.randint(1,6)))

















