class Player(object):
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        print('11111')


user = Player('lys', 24, '北京')
print(user.name,user.age,user.city)
print(user.__dict__)

class weapon(object):
    def __init__(self, name, damage, level):
        self.name = name
        self.damage = damage
        self.level = level

gun = weapon('magic', 1000, 3)
print(gun.__dict__)