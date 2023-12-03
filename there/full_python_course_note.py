

friends = ["alld", "dsd", "dkkd", "fsad"]
best_friend = "alld"


for friend in friends:
    if friend == best_friend:
        print(f"{best_friend}  is in friends ,I got you")

# %%
budget = 100

sandwich = 5

for s in range(19):  # 0~18
    print(f"you bopught a sandwich. ")
    budget -= sandwich
print(budget)
# %%
budget = 100
sandwich = 5

while True:
    print(f"you bopught a sandwich. ")
    budget -= sandwich
    if budget == 0:
        break
print(budget)

# %%
# Elevator Program

while True:

    answer = int(input("key"))
    if answer == "out":
        print("Exiting")
        break
    else:
        if answer > 0 and answer <= 10:
            print(answer)
        else:
            print(f"{answer}  is over")
            print("bye bye")
            break

# %%


def special_count(stop, step):
    for i in range(1, stop+1, step):
        print(f"Special count{i}")


special_count(5, 1)

# %%
# 勾股定理


def is_pyth_triple(a, b, c):
    num_ab = a**2+b**2
    num_c = c**2
    if num_ab == num_c:
        print(f"The conbination of : {a},{b},{c} supports pyth law!")
    else:
        print(f"The combination of:{a},{b},{c} doesn't")


is_pyth_triple(3, 4, 5)
is_pyth_triple(12, 13, 15)
is_pyth_triple(7, 24, 25)
# %%


def square_my_number(num):
    result = (num**2)

    return print(f"hi+{result}")


square_my_number(9)

# %%


# %%
def numbers(max):
    sum = 0
    for n in range(1, max+1):
        sum += n
    return sum


value = numbers(int(input("請輸入你希望運算從 1 加總到幾的數字： ")))
# 因為這時候輸入的數字是字串，記得加入 int 把字串變成浮點數
print(value)

# %%


def hide_card(card_number):
    return card_number[-4:]


x = input("Please key you 12 digits number of your credit card")
my_card = hide_card(x)


print(f"**** ****  {my_card}")
# %%


def hide_card(card_numbers):
    cards_list = []
    for card_number in card_numbers:
        last_four_digit_number = card_number[-4:]
        formatted_credit_card = f"**** **** **** {last_four_digit_number}"
        cards_list.append(formatted_credit_card)
    return cards_list


my_card = hide_card(['123456789012', '987654321098'])
print(my_card)

# %%
x = "123456789"
z = x[-4:]
print(z)


y = []
y.append(z)
print(y)


z1 = int(z)
y1 = []
y1.append(z1)
print(y1)


# %%
#  list 裡  單一  字串元素==> list 裡的 多個元素


y = ['123']
z = []

for i in y:
    z += i

print(z)
# %%


class creditcard:
    def __init__(self, number, company, limit="399"):
        self.number = number
        self.limit = limit
        self.company = company

    def hide(self):
        print("hiding!")
        self.number = f"**** **** ****{self.number[-4:]}"


c1 = creditcard(number="1231", company="jim")
print(c1.number)
c1.hide()
print(c1.number)

# %%


class creditcard:
    limit_raise_amout = 1.5

    def __init__(self, number, limit):
        self.number = number
        self.limit = limit

    def hide(self):
        self.number = f"**** **** **** {self.number[-4]}"

    def raise_limit(self):
        self.limit = creditcard.limit_raise_amout*self.limit
        print(f"Congratulation!!{self.limit}and {self.number}")


c1 = creditcard(number="1213121312321212", limit=1000)
c1.raise_limit()
c2 = creditcard(number="999999999999999", limit=1000)
c2.raise_limit()

# d
