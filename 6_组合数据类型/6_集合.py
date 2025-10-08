s = set()
print(s, type(s))

s = {1,2,3,4}
print(s, type(s))

s = set('123')
print(s)

s.update({2,3,4,5,6})
print(s)


# 交集
s2 = { 5, 6, 7}
print(s & s2)

print(s | s2)