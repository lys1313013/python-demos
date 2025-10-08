list1 = []
print(list1)
print(type(list1))

list2 = [1, 2, 3, True, 'hello']
print(list2)
print(list2[2])

list3 = list()
print(list3)

# 遍历
for i in list2:
    print(i)

for i, j in enumerate(list2):
    print(i, ": ", j)

list2.append("追加")
print(list2)

list2.insert(0, "第一个")
print(list2)

# 根据索引删除
list2.pop(0)
print(list2)

# 根据值集删除
list2.remove("追加")
print(list2)

list2.clear()
print(list2)

nums = [1, 2, 3, 4]
print(sum(nums))
