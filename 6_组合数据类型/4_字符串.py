s = "hello "

print(s + "lys")
print(s * 3)
print(len(s))
print(max(s), min(s))
# 查看 ASCII码
print(ord('A'))
print(ord('a'))
print(ord(' '))

# 字符串遍历
for i in s:
    print(i, end="")
print()

# 类型转换
print(str([1, 2, 3, 4]))

# api
print(s.upper())
print(s.lower())
print(s.count('l'))
print(s.strip())
print(s.split(' '))
print('#'.join(["111", "222", "333"]))

s = '文字。文字\n'
s = s.replace('\n', ' ').replace('。', ' ').strip()
print(s)

# 统计字母、数字、符号的个数
s = input('请输入：')
a,b,c = 0,0,0
for i in s:
    if i.isdigit():
        b += 1
    elif i.isalpha():
        a += 1
    else:
        c += 1
print(a, " ", b, " ", c)
