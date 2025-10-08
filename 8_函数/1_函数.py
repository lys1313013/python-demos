def f():
    print('python')
f()


def sum_2(a, b):
    print(a + b)
sum_2(1, 2)


# 两个参数
def sum_return(a, b):
    return a + b
print(sum_return(1,2))

# 带默认值
def sum_default(a, b = 100):
    return a + b
print(sum_default(1))

# 多个默认值，并指定某个字段的值
def print_info(name, age = 18, gender = '男'):
    print("姓名：%s, 年龄：age： %d, 性别：%s"% (name, age, gender))
print_info('lys', 18, '男')
print_info('lys')
print_info('lys', gender= '女')

# 可变参数
def total(*args):
    result = 0
    for i in args:
        result += i
    return result
print(total(1,4,5,6,7,8))

def f(**kwargs):
    for k,v in kwargs.items():
        print(k,v)
d = {'name': 'xiaoming', 'age': 18}
f(**d)
