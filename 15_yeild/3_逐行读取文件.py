"""
逐行读取文件
"""
def read_file(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            yield line.strip()


file_path = "1_生成器.py"
for line in read_file(file_path):
    print(line)
