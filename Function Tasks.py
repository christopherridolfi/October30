def product():
    number_1 = int(input("input a number"))
    number_2 = int(input("input a second number"))
    total = number_1 * number_2
    return str(total)


print(product())


def compare():
    com_1 = int(input("Input a number"))
    com_2 = int(input("input a second number"))
    total_2 = com_1 = com_2
    if total_2 == True:
        print(True)
    else:
        print("False")


print(compare())



a = 0  #I used a, b, c for my values because the basic formula for pythagorean theorym is a2 + b2 = c2
b = 0
c = 0
bill_total = 0
bill_percentage = 0
c = 0
f = 0
import math
restart = 0
while restart == 0:  #This peice of code makes the program go continuesly unless restart is not 0.

    def option_1():
        a = float(input("What is the First side length "))
        b = float(input("what is the Second Side Length"))
        c = math.sqrt(a**2 + b**2)  # This peice of code squares the two numbers and adds them together. I did this becasue the easiest way to find the hypotonuse is to use pythagorean theorym
        print(c)
    def option_2():
        bill_total = input("What is your Total for Your Bill")
        bill_percentage = float(bill_total) * float(0.15)
        print(str("You should Tip " + str(bill_percentage)))
    def option_3():
        c_or_f = input("Do you Want to Start with Celsius or Fahrenheit")
        if c_or_f == ("Celsius"):
            c = input("What is the Temperature in Celsius")
            convert_1 = (int(c) * 9/5 +32)  #This is the formula for turning Celsius to Fahrenheit. I used this becasuse we had to convert Celsius to Degrees.
            print(str(convert_1) + " Fahrenheit")
        if c_or_f == ("Fahrenheit"):
            f = input("What is the Temperature in Fahrenheit")
            convert_2 = ((int(f) - 32) * 5/9)  #This is the Formula to turn Fahrenheit to Celsius. I used this because it was an easy formula to convert Fahrenheit to Celsius.
            print(str(convert_2) + " Fahrenheit")
    restart_input = input("do you want to stop the code")
    if restart_input == ("yes"):  #This peice of code increases restart/
        restart = restart + 1

    question_z = input("What option do you want to play")
    if question_z == "1":
        print(option_1())
    if question_z == "2":
        print(option_2())
    if question_z == "3":
        print(option_3())

