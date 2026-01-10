import multiprocessing
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
    # 使用元组方式给指定任务传参 注意：使用元组传参的时候，顺序要和方法声明的参数顺序一致
    # 顺序错误情况，报错信息为 TypeError: 'str' object cannot be interpreted as an integer
    singer = multiprocessing.Process(target=sing, args=("张三", 3))
    # 使用字典方式给指定任务传参 注意：使用字典传参的时候，key要和方法声明的参数名一致
    dancer = multiprocessing.Process(target=dance, kwargs={"num": 2, "name1": "李四"})
    singer.start()
    dancer.start()
    singer.join()
    dancer.join()
