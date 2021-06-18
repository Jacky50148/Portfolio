# 猜數字遊戲01

# 不限猜的次數

import random

answer = random.randrange(1,101) # 隨機產生1~100之間的一個數字當作答案
guess = None # 初始猜測數字為空值

while guess != answer: # 若猜測數字不等於答案
    guess = int(input("請輸入一個數字(1~100): ")) # 使用者輸入猜測數字
    if guess < answer: # 若猜測數字小於答案
        print("高一點") # 提示高一點
    elif guess > answer: # 若猜測數字大於答案
        print("低一點") #提示低一點

print("恭喜答對！") # 印出恭喜答對
