d = {
    'name': 'lys',
    'gender': 1,
    'height': 170
}

print(d)
print(type(d))

d['height'] = 180
print(d)

print('name' in d)

print(d.copy())

print(d.get('name'))

d.popitem()
d.popitem()
d.popitem()
print(d)
