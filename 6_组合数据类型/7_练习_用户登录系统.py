users = [
    {
        'name': 'lys',
        'password': '123456',
        'status': True,
    },
{
        'name': '小明',
        'password': '123456',
        'status': True,
    },
    {
        'name': '小黑',
        'password': '123456',
        'status':  False,
    },

]



error_count = 0

for i in range(3):
    name = input('请输入用户账号：')
    password = input('请输入密码：')
    flag = False
    for user in users:
        if name == user['name'] and user['status'] == False:
            print('账号已停用')
            flag = True
            break
        if name == user['name'] and password == user['password']:
            print('登录成功')
            flag = True
            break
    if not flag:
        print('登录失败')



