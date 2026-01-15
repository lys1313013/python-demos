
num = int(input("输入一个数字："))

try:
    if num == 0:
        raise RuntimeError("不允许输入0！")
    else:
        print("正常通过")
except Exception as e:
    print(f"出现了异常：{e}")
else:
    print("没有出现异常")
