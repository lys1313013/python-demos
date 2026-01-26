import time

local_time = time.localtime()
print(local_time)
# 格式化为字符串
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
print(formatted_time)
