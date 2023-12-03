# %%


import sys
Score = [87, 66, 90, 65, 70]
Total_Score = 0
for count in range(5):
    print("第%d 位學生的分數:%d " % (count+1, Score[count]))
    Total_Score += Score[count]
print("----")
print("5個學生的總分 : %d " % Total_Score)
# %%
N = 2
arr = [[None]*N for row in range(N)]
print('|a1 b1|')
print('|a2 b2|')
arr[0][0] = input('請輸入 a1:')
arr[0][1] = input('請輸入 b1:')
arr[1][0] = input('請輸入 a2:')
arr[1][1] = input('請輸入 b2:')

result = int(int(arr[0][0])*int(arr[1][1])-int(arr[0][1])*int(arr[1][0]))
print('|%d %d|' % (int(arr[0][0]), int(arr[0][1])))
print('|%d %d|' % (int(arr[1][0]), int(arr[1][1])))
print('行列式值 = %d ' % result)


# %%
# %%


# %%


class student:
    def __init__(self):
        self.name = ''
        self.Math = 0
        self.Eng = 0
        self.next = None


head = student()
head.next = None
ptr = head
Msum = Esum = num = student_no = 0
select = 0

while select != 2:
    print('(1)新增(2)離開')
    try:
        select = int(input('請輸入一個選項:'))
    except ValueError:
        print('輸入錯誤')
        print('請重新輸入')
    if select == 1:
        new_data = student()
        new_data.name = input('請輸入學生姓名')
        new_data.no = input('學號')
        new_data.Math = int(input('請輸入Math'))
        new_data.Eng = int(input('請輸入Eng'))
        ptr.next = new_data
        new_data.next = None
        ptr = ptr.next
        num += 1

ptr = head.next
print()
    

while ptr != None:
    print(f'(姓名:{ptr.name},學號: {ptr.no},Math:{ptr.Math},Eng:{ptr.Eng})')
    Msum += ptr.Math
    Esum += ptr.Eng
    student_no += 1
    ptr = ptr.next
if student_no != 0:
    print(f'平均Math:{(Msum/student_no):0.2F},平均Eng:{(Esum/student_no):0.2F}')

# %%
