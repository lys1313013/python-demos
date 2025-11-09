score = int(input("输出成绩："))

if score >= 90:
    print("优秀")
elif score >= 80:
    print('良好')
elif score >= 60:
    print('及格')
else:
    print('垃圾')

# 变量未定义直接赋值
if score > 90:
    tip = '很棒'
else:
    tip = '一般般吧'
print(tip)
