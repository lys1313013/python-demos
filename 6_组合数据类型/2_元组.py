tuple1 = (1, 2, 3, True, 'hello')
print(tuple1)

#
print(tuple1.count(2))
# 输出 2， 原因 True 被视为整数 1
print(tuple1.count(1))

# 遍历
for index, value in enumerate(tuple1):
    print(index, " ", value)
