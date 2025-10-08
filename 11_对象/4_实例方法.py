class Player(object):
    numbers = 0 # 类属性
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        print('11111')
        Player.numbers += 1
    def show(self):
        print('我是'+ self.name)

user1 = Player('lys', 18, '北京')
print(user1.__dict__)
user1.show()