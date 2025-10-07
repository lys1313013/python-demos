n = 5
for i in range(n):
    print(i)

#
print("九九乘法表：")
m = 9
n = 1
for i in range(9):
    for j in range(i + 1):
        print("%d * %d = %d" %((j + 1), (i + 1), ((j + 1) * (i + 1))), end = '  ')
    print()
