def hello_world():
    print("Hello World")


hello_world()



def addition(a, b):
    return a + b

print(addition(3,4))


def multiply(c,d):
    return c * d
print(multiply(2,4))


def grade_percent():
    value = int(input("What is your Grade"))
    if value < 50 and value > 0:
        print("F")
    elif value >= 52 and value <= 69:
        print("D")
    elif value >= 70 and value <= 79:
        print("C")
    elif value >= 80 and value <= 89:
        print("B")
    elif value >= 90 and value <= 100:
        print("A")
    if value < 0:
        print("Invalid Input")


grade_percent()






