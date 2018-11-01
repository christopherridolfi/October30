import random
import time

def f_time():
    ran = random.randint(1,5)
    time.sleep(ran)
    print("BOO")

f_time()


def tirc_treat():
    ran_2 = random.randint(1,2)
    print(ran_2)
    if ran_2 == 1:
        print("Trick")
    if ran_2 == 2:
        print("Treat")

tirc_treat()

