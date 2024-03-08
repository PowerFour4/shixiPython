import random
x = 3 # 变量就是个名字
y = 5
x, y = y, x
print(x,y)
print(r"D:\three\two\one\now")  # r“”表示原始字符串 字符串中转义字符\无效
print(520+1314)
print('520'+'1314')
print("521"*10)

x = random.getstate()
print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))
random.setstate(x)
print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))
print(0.1 + 0.2)
print(1+2j)
a = 1+2j    # pythonb包含复数
print(a.real)
print(a.imag)
print(divmod(-3,2)) # divmod返回两个变量地板除的结果和余数 注意地板除返回的是向下取整的整数 而非去除小数部分
print(divmod(2,1))
print(int(-2.5))
print(pow(2,3), 2**3)   # pow和**等价
print(pow(2,3,5))   # 当pow传入三个参数时计算的是前两个参数的幂运算结果和第三个参数进行取余运算的结果