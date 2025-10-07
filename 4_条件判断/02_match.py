score = input("输出等级（A,B,C）：")

match score:
    case 'A':
        print('优秀')
    case 'B':
        print('良好')
    case 'C':
        print('及格')
    case _:print('输入的不对')