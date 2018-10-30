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