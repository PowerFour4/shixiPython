# i = 1
# sum = 0
# while i<=1000000:
#     sum += i
#     i += 1
# print(sum)
# while True:
#     answer = input('could you stop me?')
#     if answer == 'you can':
#         break
#     print("so teried")
# day = 1
# while day<=7:
#     answer = input("学习了吗")
#     if answer != "有":
#         break
#     day += 1
# else:
#     print("恭喜")
# for i in range(9):
#     for j in range(9):
#         print(f"{i+1} x {j+1} = {(i+1)*(j+1)}")
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print(i, "x", j, "=", i*j, end=" ")
#         j += 1
#     print()
#     i += 1
for n in range (2, 10):
    for x in range(2, n):
        if n%x == 0:
            print(n, "=", x, "x", n//x)
            break
    else:
        print(n,"is a 素数")