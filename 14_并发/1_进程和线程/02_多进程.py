import multiprocessing
import time


def sing():
    for i in range(3):
        print("唱歌。。。")
        time.sleep(0.5)


def dance():
    for i in range(3):
        print("跳舞。。。")
        time.sleep(0.5)


if __name__ == "__main__":
    start = time.time()
    singer = multiprocessing.Process(target=sing)
    dancer = multiprocessing.Process(target=dance)
    singer.start()
    dancer.start()
    singer.join()
    dancer.join()
    print(f"耗时：{time.time() - start}")