class Player(object):
    def __init__(self, name):
        self._name = name
        self.__name = name

user = Player('lys')
print(user._name)
user._name = 'lys2'