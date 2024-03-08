import random

counts = 3
answer = random.randint(1, 10)
while counts > 0:
    temp = input("你猜")
    guess = int(temp)
    if guess==answer:
        print("猜对了")
        break
    else:
        if guess < answer:
            print("小了")
        else:
            print("大了")
        counts = counts - 1

print(dir(__builtins__))
