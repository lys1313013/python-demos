list1 = []
print(list1)
print(type(list1))

if not list1:
    print("列表是空的")

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

print("切片.注意:左闭右开")
print(f"截取第一个元素：{nums[:1]}")
print(f"截取第一个元素：{nums[0:1]}")
print(f"截取第二个元素：{nums[1:2]}")
print(f"截取除最后一个元素外的所有元素 {nums[:-1]}")

print("排序")
nums = [3, 1, 4, 2]
nums.sort()
print(nums)

dicts = [
    {"name": "张三", "age": 18},
    {"name": "李四", "age": 20},
    {"name": "王五", "age": 15},
]
dicts.sort(key=lambda x: x["age"])
print(dicts)
