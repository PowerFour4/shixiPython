a=bool("520")
b=bool("假")
c=bool("False")
d=bool(False)
print(a, b, c, d)
# None, False, 0, 0.0, 0j, Decimal(0), Fraction(0,1), '', (), [], {}, set(), range(0) bool的结果都是False
print(False or 0)
print(3 and 4, f"\n{1 and 3}")
e = not 1 or 0 and 1 or 3 and 4 or 5 and 6 or 7 and 8 and 9     # 逻辑判断存在短路逻辑，只有当第一个操作数无法确定逻辑运算结果时，才
                                                                # 对第二个操作数进行求值，当当前操作数可以判断逻辑运算结果时则直接返
                                                                # 回当前操作数的值
print(e)