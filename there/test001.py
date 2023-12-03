# %%
from pathlib import Path

import numpy as np

import django

while True:
    pw = 1234
    if pw == 1234:
        pw1 = int(input('請輸入密碼:\t'))
        if pw != pw1:
            print("密碼錯誤！\n")
            pw = pw1
        else:
            print("密碼正確！\n")
            break

while True:
    print("\n正確，歡迎光臨！\n")
    art = int(input('請輸入國文成績: \t'))
    math = int(input('請輸入數學成績:\t'))
    eng = int(input('請輸入英文成績:\t'))
    if art < 0 or math < 0 or eng < 0:
        print("wrong number  重新輸入")
    elif art > 100 or math > 100 or eng > 100:
        print("wrong number  重新輸入")
    else:
        sum = math + eng + art
        avg = sum / 3
        break

print(f"成績總分:{sum:10d},平均成績:{avg:15.3f}")


# %%

squares = []
for i in range(10):
    squares.append(i**2)

print(squares)

print([i**2 for i in range(10)])
# %%

import django
django.__version__

# %%

from pathlib import Path
Path('spam')/'bacon'/'eggs'

# 一樣

# open(Path('C:\\')/'Users'/'AI'/'Desktop'/'spam.py')
# open(r'C:\Users\AI\Desktop\spam.py')

Path.home()  # 家目錄
# %%
# %%
x, y = True, False

print(not x and y or x) # and >>or

# %%

import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

indices = np.array(
    [[False, False, True], [False, False, False], [True, True, False]])

print(a[indices])

#%%

y1 = "                      This is lazy\t\n         "
print(y1.strip())
print("smartphone".startswith("smart"))
print("smartphone".endswith("phone"))
print("another".find("other"))
print("cheat".replace("ch","m"))
print(','.join(["F","B","I"]))
print("ear" in "earth")

def f():
    x = 2
    return x

def g():
    y =3

print(f() is None )
print(g() is None)
print("" == None) 
print(0 == None )

r = t = 3
print(r is t )
print([3] is [3]) # 在記憶體不同位置


#%%
import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return 5 * x**2

# Create an array of x values
x = np.linspace(0, 6, 100)  # Choose a range that includes [1, 5]

# Calculate the corresponding y values
y = f(x)

# Create the plot
plt.plot(x, y, label='5x^2', color='blue')

# Shade the area under the curve between x=1 and x=5
x_fill = np.linspace(1, 5, 100)
y_fill = f(x_fill)
plt.fill_between(x_fill, y_fill, color='gray', alpha=0.5, label='Area')

# Set axis labels and legend
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Show the plot
plt.show()
