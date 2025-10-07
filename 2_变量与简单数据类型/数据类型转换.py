# 转换为整数int
s = '1024'
print(type(s))
n = int(s)
print(type(n))

# 浮点数 float --> int
f1 = 2.23
print(int(f1))

s2, s3 = True, False
print(int(s2), int(s3))

# int 转 float
i1 = 2
print(float(i1))


print("*" * 20)
print("字符串转bool")
print(bool("11"))
print(bool(""))

print("*" * 20)
print("转换为字符串")
n = 5
print(str(n))