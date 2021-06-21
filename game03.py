# 猜數字遊戲03

# 範圍1~100
# 每次猜測後會縮小猜測範圍
# 不限次數

import random

answer = random.randrange(1,101)
guess = None
a_min = 1
a_max = 100

while guess != answer:
    print("範圍:" , a_min , "~" , a_max)
    guess = (int(input("請輸入一個數字: ")))
    if guess < answer:
        a_min = guess
    elif guess > answer:
        a_max = guess

print("猜對了！")