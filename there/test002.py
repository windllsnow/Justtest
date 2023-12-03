
# %%
# 01
import random


def guessing_game():
    x = random.uniform(0, 100)

    xx1 = round(x)

    test = True
    while test:

        y = input("猜猜數字(0-99) : ")
        if y.isdigit():
            y1 = int(y)
            if (y1 >= 0 and y1 <= 99):
                if (y1 == xx1):
                    print("猜對了")
                    print(f"your number is {y1}")
                    test = False
                elif(y1 > xx1):
                    print("猜太高，重來")
                    print(f"your number is {y1}")
                else:
                    print("太低了，重來")
                    print(f"your number is {y1}")
            else:
                print("請重輸： 0-99")
        else:
            print("請重輸: 數字only")


guessing_game()

# %%
# 02
