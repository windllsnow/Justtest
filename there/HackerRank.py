

# %%
#
# HackerRank
# 
# fsaifaj
#
# %%
# %

import random as rm
a = rm.random()
print(a)


print(123)


# %%

n = int(input("輸入幾個數"))
a = 0
print("大於 5 的數 有\t")
for i in range(n):

    a = int(input("數字:"))

    if a > 5:

        print(f"{a},", end="")


# %%
n = 10


bb = []

for i in range(n):
    bb.append(i)
    print(bb)


print(bb)
print(type(bb))

# what the fuck
# 要先轉 str 再 轉

Str_bb = "".join([str(_)for _ in bb])

print(Str_bb)


# %%
if __name__ == '__main__':
    n = int(input())
    bb = []

    for i in range(1, n+1):
        bb.append(i)

    Str_bb = "".join([str(_)for _ in bb])

    print(Str_bb)
# %%
'''
List.extend(iterable) 將每個 iterator 加入 list
'''
xx = list(range(5))
print(xx)
yy = list(range(2))
print(yy)
xx.extend(yy)
print(xx)

'''
List.append(object) 將 object 加入 list
'''
xx = list(range(5))
print(xx)
yy = list(range(2))
print(yy)

xx.append(yy)
print(xx)
'''
從上面兩個例子可知道，
extend 是取出 object 的所有 element/iterator 扔進list 裡面，
而 append 則直接把 object 塞進 list 裡面，
不管 object 是哪種類型的資料結構。
'''
# %%


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    kk = []

    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                kk.append([i, j, k])
                if i+j+k == n:
                    kk.pop()
                else:
                    pass
    print(kk)

    #    確認append 裡 用原本的型態
    #   用迴圈 ，所以遇到時，必為最後一個，pop刪掉
    #    要最後果不用過程，出迴圈在print


# %%
'''.
if __name__ == '__main__':

    n = int(input("How many players?(2~10)"))
    arr = map(int, input("score?").split())

    arr1 = list(arr) # list
    arr2 = sorted(arr1)#由小到大
    arr3 = list(filter(lambda x:x<=100 and x>=-100, arr2))#設範圍
    
..........'''

#
# 

if __name__ == '__main__':
    
    n = int(input())
    arr = map(int, input().split())

    arr2 = sorted(list(arr))

    number1 = len(arr2)

    k = True
    while k:
        if n>=2 and n<= 10:
            if number1 == n:
                if arr2[-1] != arr2[-2]:
                    b1=arr2[-2]
                    print(b1)
                    k= False
                elif arr2[-1]==arr2[-2]:
                    haha=[]
                    for j in sorted(set(arr2)):
                        haha.append(j)
                    print(haha)
                    b22=haha[-2]
                    b33=haha[0]
                    if len(haha)>2:

                        print(b22)
                        k=False
                        continue
                    elif len(haha)==2:
                        print(b33)
                        k=False
                        continue
                    else:
                        continue

                else:
                    continue
            else:
                print("wrong")
        else:
            
            print("wrong")


# %%

#NESTED LISTED
# if __name__ == '__main__':
    
    



    # for _ in range(int(input())):
    #     name1 = input()
    #     score = float(input())
    #     # r={"name1",score}
    #     s3 = dict(dict(zip([name1], [score])))
    #     print(s3)
    #     print("-----========--")

    #     # dictionary = {'a': 'Apple', 'b': 'Banana', 'c': 'Cherries', 'd': 'Dragon Fruit'}

    #     r1 = s3.values()
    #     print("Type of variable r1 is: ", type(r1))

    #     r1 = list(r1)
    #     r2=list(map(int, r1))
    #     print(r2)

    #     print("Type of variable r is: ", type(r2))





#%%
if __name__ =='__main__':

    kk=[]

    n = int(input())
    for _ in range(n):
        name = input()
        score = float(input())
        s3 = dict(dict(zip([name], [score])))
        print(s3)
        print("-----========--")

        # dictionary = {'a': 'Apple', 'b': 'Banana', 'c': 'Cherries', 'd': 'Dragon Fruit'}

        r1 = s3.values()
        # print("Type of variable r1 is: ", type(r1))
        
        r1 = list(r1)
        
        r2=list(map(int, r1))
        print(r2)
        kk.append(r2)
        print("---+++++++-")

    print(kk)
        # print("Type of variable r is: ", type(r2))
    s =[]
    for j in range (n):

        s.append(kk[j][0])
        
    print(s)
    s111= sorted(s,reverse=True)
    print(s111)

    max_s111 = max(s111)

    print(max_s111)


    
    s111 = [value for value in s111 if value != max_s111]
    print(s111)

    s2_max = max(s111)
    print (s2_max) #抓第2大






'''回推原本 植 名字  ，然後  output 字典 那些項'''





#%%





#%%
    # 找出陣列中第2大值
    
    # two = []
    # for i in range(len(s111)):
    #     if s111[i] == max_s111:
    #         continue
    #     elif s111[i] < max_s111:
    #         two = s111[i]
    #         three =[]
    #         max_two = max(two)
    #         for j in range(len(two)):
                
    #             if two[j] == max_two:
    #                 continue
    #             elif two[j] < max_two:
    #                 three = two[j]
    #             else:
    #                 pass
    #     else:
    #         pass
    # print(two)
    # print(three)
        

    





            

#%%



# n = int(input())

# for _ in range(n):
#     d = int(input())
#     m = int(input())
#     c = [0] * m
    
#     # for i in range(m):
#         c[i] = int(input())
    
#     #模擬罷會
#     total = 0
#     for i in range(1, d+1):
#         #跳過星期五星期六
#         if i % 7 == 6 or i % 7 == 0:
#             continue
        
#         #只要一個罷會就加一
#         for j in range(m):
#             if i % c[j] == 0:
#                 total += 1
#                 break
        
#     print(total)

#%%

if __name__ == '__main__':
    # 输入学生人数
    n = int(input())

    # 创建一个空列表，用于存储每个学生的姓名和成绩
    students = []

    # 循环读入每个学生的姓名和成绩，并添加到 students 列表中
    for i in range(n):
        name = input()
        score = float(input())
        students.append([name, score])

    # 按照成绩从小到大排序
    students.sort(key=lambda x: x[1])

    # 找到第二小的成绩
    second_lowest_score = None
    for student in students:
        if second_lowest_score is None:
            if student[1] != students[0][1]:
                second_lowest_score = student[1]
        elif student[1] > students[0][1]:
            if student[1] < second_lowest_score:
                second_lowest_score = student[1]

    # 打印出成绩为第二小的学生姓名，如果有多个则按照字母顺序输出
    for student in sorted([s[0] for s in students if s[1] == second_lowest_score]):
        print(student)

#%%
def find_students_with_second_lowest_grade(students):
    # Extracting the grades
    grades = [grade for name, grade in students]

    # Finding the unique grades and the second lowest one
    unique_grades = sorted(set(grades))
    second_lowest_grade = unique_grades[1]

    # Finding students with the second lowest grade
    second_lowest_students = [name for name, grade in students if grade == second_lowest_grade]

    # Returning sorted list of names
    return sorted(second_lowest_students)

# Example input
students = [
    ["Harry", 37.21],
    ["Berry", 37.21],
    ["Tina", 37.2],
    ["Akriti", 41],
    ["Harsh", 39]
]

# Find and print the names of students with the second lowest grade
students_with_second_lowest_grade = find_students_with_second_lowest_grade(students)
for student in students_with_second_lowest_grade:
    print(student)


#%%

