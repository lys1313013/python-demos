import re


# 从字符串的开头开始匹配
print(bool(re.match(r'第[0-9]+章', "第1章")))
# 字符串的任意位置匹配
print(bool(re.search(r'第[0-9]+章', "第1章")))

# 前面带空格 match就为 False了
print(bool(re.match(r'第[0-9]+章', " 第1章")))
print(bool(re.search(r'第[0-9]+章', " 第1章")))


