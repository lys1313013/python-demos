def foo():
    yield 1
    print(11)
    yield 2
    print(22)


f = foo()
for i in f:
    print("for循环拿到的结果：", i)
