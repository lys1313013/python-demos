import os
import multiprocessing


def copy_file(file_name, source_dir, dest_dir):
    # 拼接源文件路径和目标文件路径
    source_path = os.path.join(source_dir, file_name)
    dest_path = os.path.join(dest_dir, file_name)

    # 打开源文件和目标文件
    with open(source_path, "rb") as source_file:
        with open(dest_path, "wb") as dest_file:
            # 循环读取源文件到目标路径
            while True:
                data = source_file.read(1024)
                if data:
                    dest_file.write(data)
                else:
                    break
    pass


if __name__ == "__main__":
    # 定义源文件夹和目标文件夹
    source_dir = "."
    dest_dir = "../复制"

    # 如果目标文件夹不存在则创建
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # 遍历文件夹
    for file_name in os.listdir(source_dir):
        # 多进程方式实现多任务拷贝
        sub_process = multiprocessing.Process(target=copy_file,
                                              args=(file_name, source_dir, dest_dir))
        sub_process.start()
