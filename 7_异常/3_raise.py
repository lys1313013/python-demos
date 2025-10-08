try:
    pwd = input('请输入你的密码：')
    if len(pwd) < 8:
        raise Exception('密码长度不够，请输入 8 位以上的密码')
    else:
        print('登录操作')
except Exception as e:
    print(e)
