# 猜數字遊戲02

# 範圍1~100
# 每次猜測後會提示高一點或低一點
# 限制次數5次

answer = random.randrange(1,101)
guess = None
num = 0
limit = 5

while guess != answer and number < limit:
    number += 1 
    guess = int(input("請輸入一個數字: "))
    if guess < answer and number < limit:
        print("高一點")
    elif guess > answer and number < limit:
        print("低一點")
       
if guess == answer:
    print("恭喜答對！")
else:
    print("挑戰失敗")
