s = set()
print("打印类型")
print(s, type(s))

s = {1,2,3,4}
print(s, type(s))

print("字符串转集合")
s = set('abc')
print(s)

print("往集合添加一个元素")
s.add('d')
print(s)

print("往集合中添加多个元素")
s.update({'c', 'd', 'f'})
print(s)


print("取交集")
s2 = {'d', 'c'}
print(s & s2)

print("取并集")
print(s | s2)