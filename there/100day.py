# %%

# ----------DAY1----------

# %%

# 集合的 pop()

import re
from replit import clear
import numpy as np
from timeit import default_timer as timer

import random as r
import random as rad
import random
from os import name
print('='*20+'第'+'頁總共有'+'筆資料'+'='*10)  # 黏在一起
print('='*20, '第', '頁總共有', '筆資料', '='*10)  # ，等於 空格

print(len('95637+12444'))  # '  ' 字元長度(個數)
# %%


# list.pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
list1 = ['Google', 'Runoob', 'Taobao']
list_pop = list1.pop(1)
print(f"删除的项为 :{list_pop}")
print(f"列表现在为 : {list1}")

print("_"*58)

# 字典的 pop()
site = {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
pop__obj = site.pop('name')
print(pop__obj)
print(site)

print("_"*58)

# 集合的 pop()
# 执行下面的代码,并查看输出结果:
print('pop()函数的输出结果 看这里:')
s1 = {4, 2, 1, 5}  # 集合里只有数字
s2 = {'你', '我', '他'}  # 集合里无数字
s3 = {3, 2, 4, '你', 'X'}  # 集合里既有数字又有非数字
s1.pop()  # 元素是数字时, 删除最小的数字, 其余数字升序排列
s2.pop()  # 元素非数字时, 随机删除一个元素, 其余元素随机排序
s3.pop()  # 元素既有数字又含非数字时, 如果删除的是数字, 则一定删最小的, 否则随机删除一个非数字元素
print(s1)
print(s2)
print(s3)  # 这个代码执行后, 输出的结果是随机的
'''
总结:

1、如果集合的元素都是数字, 删除时, 删掉的是最小的数字, 其余数字升序排列

2、如果集合的元素是非数字, 删除时, 删掉的是随机的元素, 其余元素随机排列

3、如果集合里既有数字又有非数字元素, 删除时:

若删掉的是数字, 则一定是删掉了最小的, 其他数字升序排列, 非数字元素随机排列;
若删掉的非数字, 则一定是随机删掉了一个, 其他数字升序排列, 非数字则随机排列.

'''
# %%

numbers = [100, 10, 21, 35, 40, 50]

result = [num + 3 for num in numbers if num % 7 == 0]  # 能除與7 的數字+3
print(result)

# %%

print('Hello \t world \n \t'*5)
print("Hello\t" + input("What is your name?") + "\t!")


# %%
x = input("What is your name?  ")
print(f"Your name is  {x:30s}  ")
print(f"共有{len(x):10d}字母")

# %%
a = input("a:")
b = input("b:")

c = a
a = b
b = c

print("a="+a)
print("b="+b)

# %%
city = input("Where are you come from?  ")
country = input("Where are you grew up?  ")
pet = input("What kind of pets do you ever have?  ")

print(
    f"Let me introduce your new band name can be  {city:4s} {country:4s} {pet:4s} band!  ")

# %%

# ------------DAY2-----------------


# %%
print("Hello"[0])

print((10_10.10)+1.0)
q11 = 'abbey Road'

print(q11[4]+q11[5]+q11[6])  # 空白鍵 也算

# %%
w = str(input("Please  key  two_digit_number:"))
w1 = w[0]
w2 = w[-1]
w11 = int(w1)
w22 = int(w2)
print(f"your number counter is  {w11+w22}")

# %%

we = int(input("What is your current  age?   "))
totallife = 90

months = int((totallife-we)*12)
weeks = int((totallife-we)*52)
days = int((totallife-we)*365)
print("If you can live 90 years! And  \n")
print(
    f"You'll have {days:1d} days,{weeks:1d} weeks and {months:1d} months left")


# %%
poi = int(input("ANy number which you like:"))

sumq = 0

for ii in str(poi):
    sumq += int(ii)


print(sumq)

# %%


def each_unit_sum(number):
    """
    :param number :
    :return:
    """

    sum_value = 0
    for item in str(number):
        sum_value += int(item)
    return sum_value


print(each_unit_sum(1234))


# %%

s1 = int(input("Begining?(yes=1,no=0)"))
s2 = bool(s1)

while s2 != False:

    print("Welcome to the tip calculator! ")
    x1 = float(input("What was the total bill which you had? "))
    y1 = float(input("How many people to split the bill? "))
    z1 = float(input("What percentage tip would you like to give?(10,12,15) ?  "))
    t1 = float((x1/y1)*(100+z1)/100)
    print(f"Each person should pay{t1:10.2f} ")

    s1 = int(input("this repl has exited, run again?(yes=1,no=0)"))
    s2 = bool(s1)


# %%

# ------------DAY3-----------------

# %%

xx = int(input('Which number you want to check? (Integer) '))
if xx == 0:
    print(f'your number is {xx} , is not even and odd number')
elif xx % 2 == 0:
    print("your number is even number")
else:
    print('your number is odd  number ')


# %%
# ____________門票_____________
print("Welcome to the rollercoaster!\m ")
heighter = int(input('What is your height in cm? '))
bill = 0

if heighter >= 120:
    print(' You can ride the rollercoaster! \n ')
    age = int(input("What is your age? "))
    if age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    elif age >= 18:
        bill += 12
        print("adult tickets $12 once")
    elif age >= 12:
        bill += 7
        print("Youth tickets $7 once")
    else:
        bill += 5
        print("Child tickets $5 once")

    wants_photos = input("Do you want a photo taken ? Y or  N. ")
    if wants_photos == "Y" or wants_photos == "y":
        bill += 3
    print(f'you bill is {bill} dollars')
else:
    print("Sorry,you have to grow taller before you can ride")


# %%
# ____________閏年_______________*****__________難__

zzz = int(input("This  year is ?  "))
if zzz % 4 == 0:
    if zzz % 100 == 0:
        if zzz % 400 == 0:
            print(f"This year {zzz} is Leap year")
        else:
            print(f"This  year {zzz} is not Leap year")
    else:
        print(f"This  year {zzz} is  Leap year")
else:
    print(f"This  year {zzz} is not Leap year")

# %%
print("Welcome to Python Pizza Deliveries! ")
size = input("What siz pizza do you want? S  ,M ,or  L")
add_peperoni = input("Do you want pepperoni? Y or N")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == "S":
    bill += 15
    if add_peperoni == "Y":
        bill += 2
        if extra_cheese == "Y":
            bill += 1
            print(f"Your final bills is ${bill}")
        else:
            print(f"Your final bills is ${bill}")
    else:
        print(f"Your final bills is ${bill}")
elif size == "M":
    bill += 20
    if add_peperoni == "Y":
        bill += 3
        if extra_cheese == "Y":
            bill += 1
            print(f"Your final bills is ${bill}")
        else:
            print(f"Your final bills is ${bill}")
    else:
        print(f"Your final bills is ${bill}")
else:
    bill += 25
    if add_peperoni == "Y":
        bill += 3
        if extra_cheese == "Y":
            bill += 1
            print(f"Your final bills is ${bill}")
        else:
            print(f"Your final bills is ${bill}")
    else:
        print(f"Your final bills is ${bill}")
# s 15  2 1
# m 20  3 1
# l 25  3 1

# %%
print("Welcome to Python Pizza Deliveries! ")
size = input("What siz pizza do you want? S  ,M ,or  L")
add_peperoni = input("Do you want pepperoni? Y or N")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25
if add_peperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is ${bill}")


# %%
# ________________LOVE　Caculator_____________________________

print("Welcome to the Love Calculator! ")
name1 = input("What is  your name?\n")
name2 = input("What is  their name? \n")
n1_01 = name1.lower()
n2_01 = name2.lower()
n3 = n1_01+n2_01


n31 = n3.count("t")+n3.count("r") + n3.count("u") + n3.count("e")  # int
n32 = n3.count("l")+n3.count("o") + n3.count("v") + n3.count("e")  # int

n333 = str(n31)+str(n32)   # str

n33 = int(n333)  # int


if n33 > 90 or n33 < 10:
    print(f"Yours' Love score is {n33},you go together like coke and mentos")
elif n33 >= 40 and n33 <= 50:
    print(f"Yours' Love score is {n33},you are alright together")
else:
    print(f"Yours' Love score is {n33}")

# you are alright together ( 40-50
# you go together like coke and mentos  ( <10 or >90


# %%
# ____________________Day4________________________

# %%


random_integer = random.randint(0, 1)
print(random_integer)

# 0.000000~0.99999999...
random_float = random.random()
print(random_float)

# 0.000000~4.99999999...
random_float1 = random_float*5
print(random_float1)

love_score1 = random.randint(1, 100)
print(f"Your love score is {love_score1}")

# %%

pp1 = random.randint(0, 1)
p = int(input("Please key any integer to move on! Exit please key  -1 "))
while p != -1:
    if pp1 == p:
        print('Heads')
        break
    else:
        print("Tails")
        break
print("\n Game finished")
# %%
# list

names_string = input("Give me  everyone's names , seperated by a comma.")
names1 = names_string.split(",")  # 預設一格 空格

kkk001 = random.choice(names1)
print(f" {kkk001} is your turn to buy lunch !  XDD")
# ________________上下一樣結果__________
num_item1 = len(names1)
num_cc = random.randint(0, num_item1-1)
print(f" {num_cc} is your turn to buy lunch !  XDD")


# %%
# 藏寶圖
# 題目  先 欄 後 列

row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure?")

pp22 = str(position)
x001 = pp22[1]
y001 = pp22[0]
x0001 = int(x001)
y0001 = int(y001)
map[x0001-1][y0001-1] = "x"
print("____"*10)


print(f"{row1}\n{row2}\n{row3}")
# %%

# 剪刀 石頭 布
# _________________超難______________________-------


rrr = int(input(
    "What do you want to choice? Type 0 for Rock , 1 for Paper,2 for Scissors"))
r1 = ["石頭", "布", "剪刀"]  # 給人
r2 = ["石頭", "布", "剪刀"]  # 給 機器

r2_choice = rad.randint(0, len(r2)-1)  # 數字  注意 len()-1
try:
    print(f"你出的是{r1[rrr]}")
    print(f"機器出的是{r2[r2_choice]}")

    while rrr == r2_choice:
        print("woops!,Please 重輸!")
        rrr = int(input(
            "What do you want to choice? Type 0 for Rock , 1 for Paper,2 for Scissors"))
        print(f"你出的是{r1[rrr]}")
        print(f"機器出的是{r2[r2_choice]}")
    if rrr > r2_choice:
        if r2_choice == 0 and rrr == 2:
            print("you lose")
        else:
            print("you win")
    else:
        if rrr == 0 and r2_choice == 2:
            print("you win")
        else:
            print("you lose")
except:
    print("oops GG ,game over ,because you key number not 0,1 or 2")


# %%


# _______________day5__________________


# %%


fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit+"Pie")
print(fruits)


# %%
student_heights = input("Input a list of student heights").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

# don't use  sum()、len

total_height = 0
for height in student_heights:
    total_height += height
print(total_height)

number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(number_of_students)


print(f"平均身高{total_height/number_of_students:4.4f} cm")


# %%

# _______________想一下_______________________
student_score = input("Input a list of student score").split()

for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)
highest_score = 0
for score in student_score:
    # 如[100,200,300];100>0; highest=100   =>     200>100;  highest=200...
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is :{highest_score}")

# %%
sum1 = 0
n = 0
for n in range(1, 101, 2):
    n += 1      # 1+1 3+1 .....
    sum1 = sum1+n
print(sum1)


sum2 = 0
for n in range(2, 101, 2):  # 2 4 ....
    sum2 += n
print(sum2)


sum3 = 0
for n in range(1, 101):
    if n % 2 == 0:
        sum3 += n
print(sum3)


# %%

for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0 or n % 5 == 0:
        if n % 3 == 0:
            print("Fizz")
        else:
            print("Buzz")
    else:
        print(n)


# %%

# __________________password____超難!!______________________
letterss = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numberss = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the pypassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like? \n"))
nr_numberss = int(input("How many numbers would you like? \n"))


num00 = nr_letters+nr_symbols+nr_numberss  # 確認 密碼 位數
print(num00)

l2 = r.sample(letterss, nr_letters)
s2 = r.sample(symbols, nr_symbols)  # 由 x字串中隨機n個字元   (type: list)
n2 = r.sample(numberss, nr_numberss)


fin2 = l2+s2+n2       # list 相加

print(fin2)

kk = r.sample(fin2, 6)  # 取6個 取後不放回
print(kk)
StrQ = "".join(kk)      # list 轉 str
print(f"你的新密碼: \t {StrQ} \t")

# %%
# __________________password____超難!!______________________
letterss = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numberss = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the pypassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like? \n"))
nr_numberss = int(input("How many numbers would you like? \n"))

# _________________________________________________easy__________________________________
password = ""
for char in range(1, nr_letters+1):
    password += r.choice(letterss)
for char in range(1, nr_symbols+1):
    password += r.choice(symbols)
for char in range(1, nr_numberss+1):
    password += r.choice(numberss)
print(password)


# %%

# %%
# __________________password____超難!!______________________
letterss = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numberss = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the pypassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like? \n"))
nr_numberss = int(input("How many numbers would you like? \n"))


# _________________________________________________HARD__________________________________

password_list1 = []
for char in range(1, nr_letters+1):
    password_list1 += r.choice(letterss)
for char in range(1, nr_symbols+1):
    password_list1 += r.choice(symbols)
for char in range(1, nr_numberss+1):
    password_list1 += r.choice(numberss)
print(password_list1)

r.shuffle(password_list1)
print(password_list1)
password1 = ""
for char in password_list1:
    password1 += char
print(f"Your password  is {password1}")

# %%
# _________________________________________DAY  6____________________________________


# %%

# def
# w hile   Loop


# %%

# __________________________________DAY7___________________________________________


# %%

# __________劊子手___超難 =='''  //我的mind  都扣1  出去再判斷

word_list = ["ardvark", "baboon", "camel"]

choice_word = random.choice(word_list)
print(f"pssst, the solution is {choice_word}.")

display = []
word_length = len(choice_word)

for _ in range(word_length):
    display += "_"
print(display)


game_times = 0

while game_times < 6:

    guess = input("Guess a letter:").lower()
    print(f"your letter you key one second before is' {guess} ' ")

    for position in range(word_length):
        letter = choice_word[position]

        if letter == guess:
            display[position] = letter
    print("The rusult is \n")
    print(display)
    game_times += 1
    if "_" not in display:
        game_times += 6
        print("your win")

if game_times == 6:
    print("you lose, die!")
else:
    print("Concretulation")


# %%
# __________劊子手___超難 ==''' 扣命

word_list = ["ardvark", "baboon", "camel"]

choice_word = random.choice(word_list)
print(f"pssst, the solution is {choice_word}.")

display = []
word_length = len(choice_word)

for _ in range(word_length):
    display += "_"
print(display)


end_of_game = False
lives = 6

while end_of_game == False:

    guess = input("Guess a letter:").lower()
    print(f"your letter you key one second before is' {guess} ' ")
    for position in range(word_length):
        letter = choice_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in choice_word:

        lives -= 1  # bug 是 如果輸入一樣 無限迴圈
        if lives == 0:
            end_of_game = True
            print("you lose!")

    print("The rusult is \n")
    print(f"{''.join(display)}")

    if "_" not in display:
        end_of_game == True
        print("your win")


# %%

# __________劊子手___超難 ==''' 扣命 final
# 有bug  成功無法  跳出  ，一定要失敗  =='''

word_list = [
    'abruptly',
    'absurd',
    'abyss',
    'affix',
    'askew',
    'avenue',
    'awkward',
    'axiom',
    'azure',
    'bagpipes',
    'bandwagon',
    'banjo',
    'bayou',
    'beekeeper',
    'bikini',
    'blitz',
    'blizzard',
    'boggle',
    'bookworm',
    'boxcar',
    'boxful',
    'buckaroo',
    'buffalo',
    'buffoon',
    'buxom',
    'buzzard',
    'buzzing',
    'buzzwords',
    'caliph',
    'cobweb',
    'cockiness',
    'croquet',
    'crypt',
    'curacao',
    'cycle',
    'daiquiri',
    'dirndl',
    'disavow',
    'dizzying',
    'duplex',
    'dwarves',
    'embezzle',
    'equip',
    'espionage',
    'euouae',
    'exodus',
    'faking',
    'fishhook',
    'fixable',
    'fjord',
    'flapjack',
    'flopping',
    'fluffiness',
    'flyby',
    'foxglove',
    'frazzled',
    'frizzled',
    'fuchsia',
    'funny',
    'gabby',
    'galaxy',
    'galvanize',
    'gazebo',
    'giaour',
    'gizmo',
    'glowworm',
    'glyph',
    'gnarly',
    'gnostic',
    'gossip',
    'grogginess',
    'haiku',
    'haphazard',
    'hyphen',
    'iatrogenic',
    'icebox',
    'injury',
    'ivory',
    'ivy',
    'jackpot',
    'jaundice',
    'jawbreaker',
    'jaywalk',
    'jazziest',
    'jazzy',
    'jelly',
    'jigsaw',
    'jinx',
    'jiujitsu',
    'jockey',
    'jogging',
    'joking',
    'jovial',
    'joyful',
    'juicy',
    'jukebox',
    'jumbo',
    'kayak',
    'kazoo',
    'keyhole',
    'khaki',
    'kilobyte',
    'kiosk',
    'kitsch',
    'kiwifruit',
    'klutz',
    'knapsack',
    'larynx',
    'lengths',
    'lucky',
    'luxury',
    'lymph',
    'marquis',
    'matrix',
    'megahertz',
    'microwave',
    'mnemonic',
    'mystify',
    'naphtha',
    'nightclub',
    'nowadays',
    'numbskull',
    'nymph',
    'onyx',
    'ovary',
    'oxidize',
    'oxygen',
    'pajama',
    'peekaboo',
    'phlegm',
    'pixel',
    'pizazz',
    'pneumonia',
    'polka',
    'pshaw',
    'psyche',
    'puppy',
    'puzzling',
    'quartz',
    'queue',
    'quips',
    'quixotic',
    'quiz',
    'quizzes',
    'quorum',
    'razzmatazz',
    'rhubarb',
    'rhythm',
    'rickshaw',
    'schnapps',
    'scratch',
    'shiv',
    'snazzy',
    'sphinx',
    'spritz',
    'squawk',
    'staff',
    'strength',
    'strengths',
    'stretch',
    'stronghold',
    'stymied',
    'subway',
    'swivel',
    'syndrome',
    'thriftless',
    'thumbscrew',
    'topaz',
    'transcript',
    'transgress',
    'transplant',
    'triphthong',
    'twelfth',
    'twelfths',
    'unknown',
    'unworthy',
    'unzip',
    'uptown',
    'vaporize',
    'vixen',
    'vodka',
    'voodoo',
    'vortex',
    'voyeurism',
    'walkway',
    'waltz',
    'wave',
    'wavy',
    'waxy',
    'wellspring',
    'wheezy',
    'whiskey',
    'whizzing',
    'whomever',
    'wimpy',
    'witchcraft',
    'wizard',
    'woozy',
    'wristwatch',
    'wyvern',
    'xylophone',
    'yachtsman',
    'yippee',
    'yoked',
    'youthful',
    'yummy',
    'zephyr',
    'zigzag',
    'zigzagging',
    'zilch',
    'zipper',
    'zodiac',
    'zombie',
]

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = '''
 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/    '''


print(logo)


end_of_game = False
lives = len(stages)-1


chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []
print(f"pssst, the solution is {chosen_word}.")
for _ in range(word_length):
    display += "_"
print(display)


while not end_of_game:

    guess = input("Guess a letter:").lower()
    clear()

    if guess in display:
        print(f"you've already guessed{guess}")

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter
    print(f"{''.join(display)}")

    if guess not in chosen_word:
        print(
            f"you guessd{guess},that's not in the word. your lost your life ")
        lives -= 1  # bug 是 如果輸入一樣 無限迴圈
        if lives == 0:
            end_of_game = True
            print("you lose!")

    if "_" not in display:
        end_of_game == True
        print("your win")

    print(stages[lives])

# fuck  fuck yes  >_<
# fuck  fuck yes  >_<


# %%

# ----Day8----------------
# -----函數--
# %%
def greet(a, b, c):

    print("hello")
    print("wear")
    print("dread")
    return print(f'hello ! your answers is {a*b*c}')


def greet23(a, b, c):

    return f'hello ! your answers is {(a*b*c)**2}'


greet(1, 2, 3)
greet23(1, 2, 3)


# %%
# prime number 質數


def prime_check(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number!")
    else:
        print("It's not a prime number!")


o = int(input("Check your number: "))
prime_check(number=o)


# %%


# %%

# Caesar Cipher

key = True

while key:

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input(
        "Type 'encode'  to encrypt, type 'decode' to decrypt(make sure your word correct!!!): \n")
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number(1~26): \n"))

    def caesar(start_text, shift_amount, cipher_direction):
        end_text = ""
        shift_amount = shift_amount % 26
        if cipher_direction == "decode":
            shift_amount *= -1
        for char in start_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift_amount
                end_text += alphabet[new_position]
            else:
                end_text += char
        print(f"Here is the {direction}d result: {end_text}")

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    ww = input("Want to play again ? (please answer  'yes' or 'no')")
    if (ww == "yes") | (ww == "YES") | (ww == "Yes"):
        key = True
    elif (ww == "no") | (ww == "NO") | (ww == "No"):
        key = False
        print("Bye.\n")

print("Bye!")


# %%
# Day 9  Dictionary & Nesting

# %%

program = {
    "bug": "I'm a bug",
    "function": "I'm a function",
    "loop": "I'm a loop"
}

for keyy in program:
    print(keyy)
    print(program[keyy]+"\n")


# %%


# Grading Program

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}


student_grades = {}

for j in student_scores:
    score = student_scores[j]
    if score > 90:
        student_grades[j] = "Outstanding"
    elif score > 80:
        student_grades[j] = "Exceeds Expectations"
    elif score > 70:
        student_grades[j] = "Acceptable"
    else:
        student_grades[j] = "Bye!!!!!!!!!!!"


print(student_grades)

# %
# %%

# Nesting

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visited": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visited": 55,
    },
]


def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["cities_visited"] = cities_visited
    new_country["total_visited"] = times_visited
    travel_log.append(new_country)


add_new_country("Russian", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)


# %%
# Q&A
dict44 = {
    "a": 1,
    "b": 2,
    "c": 3,

}

dict44[1] = 7


print(dict44)

for k in dict44:
    dict44[k] += 1
    print(dict44[k])


# %%
bids = {}
bid__finished = False


def find11(bidding):
    highest_bid = 0
    winner = ""
    for bidder in bidding:
        bid_amount = bidding[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"winner is {winner} with a bid of ${highest_bid}")


while not bid__finished:
    a = input("your name: ")
    b = int(input("Bid price? $ "))

    bids[a] = b
    continue00 = input("Are there any other bidders? Type 'yes' or 'no'")
    if continue00 == "no":
        bid__finished = True
        find11(bids)
    elif continue00 == "yes":
        clear()

# %%
# %%

# _____________________DAY__10____________________
# function WITH output
# %%


def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "NO inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result : {formated_f_name} {formated_l_name}"


print(format_name(input("your first name?"), input("your last name?")))
# %%


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year")
                return False
            else:
                print("Not leap year")
                return True
        else:
            print("Leap year")
            return False
    else:
        print("Not leap year")
        return True


def days_in_months(year, month):
    month_days_01 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_days_02 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) == True:
        return month_days_01[month-1]
    else:
        return month_days_02[month-1]


year = int(input("Enter year: "))
month = int(input("Enter month: "))
days = days_in_months(year, month)
print(days)

# %%
# Docstrings
# """ 文檔字串"""


# %%
def my(a):
    if a < 40:
        return
        print("TT")
    if a < 80:
        return "pass"
    else:
        return "Great"


print(my(25))
# %%
# calculator
key1 = True
while key1:

    a = float(input("Enter your first number: "))
    print("+\n - \n *\n / \n")
    b = input("Pick an operation:")
    c = float(input("Enter your second number: "))
    d = ["+", "-", "*", "/"]

    def calculate(a, b, c, d):
        if b == d[0]:
            return a+c
        elif b == d[1]:
            return a-c
        elif b == d[2]:
            return a*c
        elif b == d[3]:
            return a/c

    answers = calculate(a, b, c, d)
    print(f"{a} {b} {c} = {answers}")

    key = input(
        f"Type 'y'  to continue calculating with{answers} , or type 'n'to start a new calculation:")
    if (key == 'y' or key == 'Y'):
        key1 = True
    elif (key == 'n' or key == 'N'):
        key1 = False
# %%


def add(n1, n2):
    return n1+n2


def sub(n1, n2):
    return n1-n2


def mul(n1, n2):
    return n1*n2


def div(n1, n2):
    return n1/n2


operation = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}


def calculator():
    num1 = float(input("first number: "))
    for symbol in operation:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation:(+,-,*,/)")

        num2 = float(input("second number: "))

        calculation_function = operation[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol}{num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to exit") == 'y':
            num1 = answer
            calculator()
        else:
            should_continue = False


calculator()


# %%
# day 11
# blackjack capstone Project  難
##
# %%
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# cards  還沒用


def a1():

    n1 = random.randint(1, 11)
    n2 = random.randint(1, 11)
    return [n1, n2]


player1 = a1()
player2 = a1()
print(player1)
print(player2)

# 確認 不能 重複4色 ，52 張????how?
# ace = 1 & 11


p1_add = player1[0]+player1[1]
p2_add = player2[0]+player2[1]

# while  加牌


def cal_01(p1_add, p2_add):
    if p1_add > 21:
        return f"p2 get {p2_add} __p2 win."
    elif p2_add > 21:
        return f"p1 get {p1_add} __p1 win."
    elif p1_add > p2_add:
        return f"p1 get {p1_add} __p1 win."
    elif p2_add > p1_add:
        return f"p2 get {p2_add} __p2 win."
    elif p2_add == p1_add:
        return f"p1 = p2  is {p1_add} = {p2_add}"


answer_001 = cal_01(p1_add, p2_add)
print(answer_001)


# %%

#~~~~~~~~~難到爆~~~

import random
from replit import clear
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0 :
        return "win with Blackjack"
    elif user_score > 21:
        return "you lose, burst!"
    elif computer_score > 21:
        return" you win , it burst!"
    elif user_score > computer_score:
        return "you win"
    else:
        return "you lose"



def play_game():
    user_cards = []
    computer_cards =[]
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f" your cards: {user_cards},current score :{user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or  user_score > 21:
            is_game_over = True

        else:
            user_should_deal =  input("type 'y' to get another card, type 'n' to pass")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over =True


    while computer_score != 0 and computer_score < 17 :
        computer_cards.append(deal_card())

        computer_score = calculate_score(computer_cards)

    print(f"your final hand:{user_cards},final score :{user_score}")
    print(f"computer final card: {computer_cards},final score :{computer_score}")
    print(compare(user_score,computer_score))
while input("Do you want to play a game of Blackjack? type'y' or 'n' ") == "y":
    clear()
    play_game()







    
# %%
#____________________day 12__________________________________

# %%
print()











# %%

# %%
print("-------------------------------------------------------")
# %%

# 微  學 習  array
# Example 1 : NumPy Array性能測試


# 1 先建立空的list再一一擺入元素
start = timer()  # 計時開始
for x in range(100):  # 重複做100次
    j = []  # 產生一個空的list
    for i in range(10000):
        j.append(i**2)  # 將平方數一個個擺入list
end = timer()  # 計時結束
print(end - start)  # 計算時間差

# 2 以list comprehensions方式直接建立平方數list
start = timer()  # 計時開始
for x in range(100):  # 重複做100次
    j = [i**2 for i in range(10000)]  # 直接建立平方數list
end = timer()  # 計時結束
print(end - start)  # 計算時間差

# 3 直接建立Array
start = timer()  # 計時開始
for x in range(100):  # 重複做100次
    i = np.arange(10000)  # 建立一個0~9999的Array
    j = i**2  # 將Array裡面的每個元素平方
end = timer()  # 計時結束
print(end - start)  # 計算時間差
# %%
# %%


# Example 2 : NumPy Array基本運算

# step 1：1維的等差陣列
a = np.arange(0, 4.0, 0.5)  # 類似python內建的range，只是輸出是array的資料型態
print(a)  # 輸出為：[ 0.  0.5  1.  1.5  2.  2.5  3.  3.5]
print(type(a))  # 輸出為：<class 'numpy.ndarray'>

# step 2：修改陣列中的內容
a[0] = 5  # 將array a中index為0的元素重新指定數值為5
a[-1] = 100  # 將array b中的最後一個元素改成100
print('array a = ', a)  # 輸出為：[ 5.  0.5  1.  1.5  2.  2.5  3.  100.]

# step 3：先建立list再將轉為array
b = np.array(range(10))  # range(10)為list的資料型態，利用array( )指令就可轉換為array
print(type(range(10)))  # 輸出為：<class 'range'>
print(type(b))  # 輸出為：<class 'numpy.ndarray'>
print('array b = ', b)  # 輸出為：[0 1 2 3 4 5 6 7 8 9]

# step 4：對array中的元素進行運算
c = a[1:-1]**2  # 將array中index為1~-1取出來，然後每個元素平方
print(c)  # 輸出為：[ 0.25  1.  2.25  4.  6.25  9.]
d = a[5:]*0.5  # 將array中index為5以後的元素取出來，然後每個元素乘0.5
print(d)  # 輸出為：[1.25  1.5  50.]

# step 5：兩個array之間的運算
e = a[:-1] + b[-7:]  # 將array a和array b的index 0~-1與-7~最後元素取出相加
print(e)  # 各取出a和b七個元素後相加，請注意取出的個數要一樣多
# 這裡我們接著介紹2維的array，或者你暫時把它理解為矩陣也沒什麼問題。以下我們給幾個簡單的範例：
# %%


# Example 3 : 2維的Array
a = np.array([[1, 2], [3, 4]], dtype=float)  # 建立一個2*2的array，裡面元素型態為float
print(a)  # 印出array a
print(type(a))  # 印出a的資料型態
print(a.shape)  # 印出a的形狀，輸出結果為(2,2)

# # 從程式執行的結果會發現a是一個 2×2 的矩陣，在數學上的表示法為：

# a=(1324)
# 下指令a.shape可給出a形狀，得到它是一個2列（row）、2行（column）的矩陣。其內容為，第1個 row 為 (12)、第2個 row 為 (34)；第1個 column 為 (13)、第2個 column 為 (24)。
# 除此之外，如果要將這個陣列中的元素更改、取出或做任何運算，則必須知道這個 array 的 index。如果是2維的就會有兩組 index 來表示各個元素的位置。如下圖所示：紅色數字為兩組 index，axis 為 array 預設的軸方向


# %%


# Example 4 :  2維Array的索引值
a = np.array([[1, 2], [3, 4]], dtype=float)  # 建立一個2*2的array，裡面元素型態為float
print('the element at 1st row and 1st column = ', a[0][0])  # 第1列，第1行 = 1.0
print('the element at 1st row and 2nd column = ', a[0][1])  # 第1列，第2行 = 2.0
print('the element at 2nd row and 1st column = ', a[1][0])  # 第2列，第1行 = 3.0
print('the element at 2nd row and 2nd column = ', a[1][1])  # 第2列，第2行 = 4.0
# 另外在科學上也常常利用到求和的指令 sum()，就是將矩陣中的元素加總，這常用在求平均值、向量量值、質心或重心位置…等。以下我們作簡單練習：
# %%


# Example 5 : 2維Array內的元素求和
a = np.array([[1, 2], [3, 4]], dtype=float)  # 建立一個2*2的array，裡面元素型態為float
b = np.sum(a, axis=0)  # 將矩陣的元素沿著直的的方向加起來，並以1維array儲存結果
c = np.sum(a, axis=1)  # 將矩陣的元素沿著橫的的方向加起來，並以1維array儲存結果
print(b, b.shape)  # 可得array b為[4. 6.]的1維array，b.shape = (2,)
print(c, c.shape)  # 可得array c為[3. 7.]的1維array，c.shape = (2,)
# 1維和2維用shape指令取出陣列形狀的差異：

# 同學們會發現在這段段程式中，如果有一個1維的array裡面含有N個元素，則該陣列的shape為(N,)，這裡的N指的是元素的個數。雖然它看起來和1列N行的矩陣很像，但是它們實際上差了一個維度，1列N行的矩陣是2維的！舉例來說：

# 1維5個元素的array為：a = np.array([1, 2, 3, 4, 5]) → a.shape = (5,)
# 2維1列N行的矩陣為：b = np.array([[1, 2, 3, 4, 5]]) → b.shape = (1,5)

# 同學該可以明顯看出其差異，1維的array只要用1層中括號，而2維的array需要用到兩層中括號。

# 這裡還有一些常見NumPy內建可以快速製造array的指令們：
# %%
# Example 6 : Array其他常用內建指令
print(np.zeros((5, 3)))  # 建立shape為(5,3)，每個元素都是0的Array
print(np.ones((5, 3)))  # 建立shape為(5,3)，每個元素都是1的Array
print(np.diag([1, 2, 3]))  # 建立主對角線元素依序為1,2,3的方陣，shape為(3,3)
print(np.random.rand(5, 5))  # 建立shape為(5,5)的Array，每個元素介於0~1之間均勻隨機產生
print(np.random.randn(5, 5))  # 建立shape為(5,5)的Array，所有元素的產生呈常態分佈，平均值為0、標準差為1
# 更多 NumPy Array 的內建指令請參考 NumPy 官方網站：
# Array creation routines : 初階的陣列產生與控制指令。

# Random sampling : 以陣列產生隨機亂數的各種指令，包含眾多分佈函數。

# Linear algebra : 以陣列進行線性代數等矩陣相關的運算指令。

# 最後我們介紹更進階的用法－array 的維度擴充，例如：將1維 array 擴充成2維、2維擴充為3維。這裡只用到一個簡單的指令叫做「newaxis」，就可以輕易達成這件事。以下我們看看範例程式：
# %%


# Example 7 : Array的維度擴充 - 1維到2維
a = np.array([1, 2, 3, 4])  # 建立1維的array
b = a[:, np.newaxis]  # 意義等同array([[1], [2], [3], [4]])
c = a[np.newaxis, :]  # 意義等同array([[1, 2, 3, 4]])
print('array b = ', b, 'shape of b is', b.shape)  # 印出b和其形狀
print('array c = ', c, 'shape of c is', c.shape)  # 印出c和其形狀
# 以上程式執行之後你會發現，增加一個維度事實上就是多了一層中括號，只是有兩種括的方式。[:, newaxis]是將第一層中括號內的每個元素括起來；而[newaxis, :]是將第一層中括號內的所有元素整個括起來。這就使得原來1維4個元素的array分別變成shape是(4,1)和(1,4)的2維array，示意圖如下：


# 根據前面的原理，我們試試將array的維度由2維擴充到3維，請執行以下程式碼：
# %%


# Example 8 : Array的維度擴充 - 2維到3維
# 建立shape為(5,3)的array
d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# 意義同array([[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]], [[10, 11, 12]]])
e = d[:, np.newaxis]
# 意義同array([[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]])
f = d[np.newaxis, :]
print(d, d.shape)  # 印出d和其形狀
print(e, e.shape)  # 印出d[:, newaxis]和其形狀
print(f, f.shape)  # 印出d[newaxis, :]和其形狀
print(e[1][0][2])  # 印出d[:, newaxis]的第2列、第1行、第3排之元素 = 6
print(f[0][1][1])  # 印出d[newaxis, :]的第1列、第2行、第2排之元素 = 5
# 以下我們用圖示來表示3維array的樣子，同學對照立體圖形看會比較具體：


# 這裡的規則我們從程式碼拆解來看，請切記中括號要一層一層拆下去，每個逗點隔開的就是一個元素，看完一層後再繼續往內。以下舉例說明：


# 紅色中括號[…]，稱為第一層，這裡面放的元素會往axis = 0的方向擺，因此成為第1列、第2列…。藍色中括號[…]，稱為第二層，這裡面放的元素會往axis = 1的方向擺，故成為第1行、第2行…。綠色中括號[…]，稱為第三層，這裡面放的元素會往axis = 2的方向擺，故成為第1排、第2排…。所以你可以看出來，d[:, newaxis]會是一個共4列、1行、3排的array。如果是以下情況，原理也相同：


# 可看出d[newaxis, :]將會是一個共1列、4行、3排的array。同學再對照上一頁的立體圖形，概念上將會清楚很多！

# 如果繼續往更高維度探討，可能很容易超出人腦的想像空間，因為我們活在3維空間。但是電腦不會，因為他只要一層一層作中括號下去就好了！


# 不過我們還是可以再想一下，
# 例如你在圖書館裡也會看到類似的結構，如上圖。
# 接著下個維度可能是「第X區」，再來是「第X樓」，再來是「第X棟」，
# 只是我們不可能一直命名下去，同學腦海中記得這種一層一層的觀念即可！
