import os

file_path = "test.txt"
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"已删除文件: {file_path}")
else:
    print(f"文件 {file_path} 不存在。")