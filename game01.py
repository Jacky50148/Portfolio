# 猜數字遊戲01

# 範圍1~100
# 每次猜測後會提示高一點或低一點
# 不限次數

import random

answer =  random.randrange(1,101)
guess = None

while guess != answer:
    guess = int(input("請輸入一個數字: "))
    if guess < answer:
        print("高一點")
    elif guess > answer:
        print("低一點")
print("恭喜答對！")
