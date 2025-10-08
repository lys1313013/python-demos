class Player(object):
    @classmethod
    def get_players(cls):  # 类方法
        print('这是一个类方法')

Player.get_players()