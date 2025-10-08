class Player(object):
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        print('子类的方法')

    def show(self):
        print('我是' + self.name)


class VIP(Player):
    def __init__(self, name, age, city):
        super().__init__(name, age, city)


user = VIP('lys',18,'北京')
user.show()