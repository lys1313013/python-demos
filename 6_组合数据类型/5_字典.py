d = {
    'name': 'lys',
    'gender': 1,
    'height': 170
}

print(d)
print(type(d))

d['height'] = 180
print(d)

print('获取值')
# 如果键不存在：会抛出 KeyError 异常。
print(d['name'])
# 如果键不存在：不会报错，而是返回 None（或指定一个默认值）。
print(d.get('name'))

print('name' in d)

print(d.copy())

print(d.get('name'))

d.popitem()
d.popitem()
d.popitem()
print(d)
