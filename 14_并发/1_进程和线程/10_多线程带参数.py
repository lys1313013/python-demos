import threading
import time


def sing(num, name):
    for i in range(num):
        print(f"{name}唱歌。。。")
        time.sleep(0.5)


def dance(num, name):
    for i in range(num):
        print(f"{name}跳舞。。。")
        time.sleep(0.5)


if __name__ == "__main__":
    # 使用元组方式给指定任务传参 注意：使用元组传参的时候，顺序要和方法声明的参数顺序一致；如果只有一个参数，也需要在元组中添加一个逗号
    singer = threading.Thread(target=sing, args=(3, "张三",))
    # 使用字典方式给指定任务传参 注意：使用字典传参的时候，key要和方法声明的参数名一致
    dancer = threading.Thread(target=dance, kwargs={"num": 2, "name": "李四"})
    singer.start()
    dancer.start()
    singer.join()
    dancer.join()
