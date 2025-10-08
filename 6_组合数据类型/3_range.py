print(list(range(10)))
print(list(range(2, 10)))
print(list(range(2, 10, 3)))

# 计算水仙花数（个位、十位和百位的三次方相加等于数字本身）
for i in range(100, 1000):
    t = str(i)
    a = int(t[2])
    b = int(t[1])
    c = int(t[0])
    if a ** 3 + b ** 3 + c ** 3 == i:
        print(i)
