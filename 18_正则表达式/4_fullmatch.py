import re

pattern = "第[0-9]章"
print(bool(re.match(pattern, '第1章')))
print(bool(re.fullmatch(pattern, '第1章')))

print(bool(re.match(pattern, '第1章 ')))
# 从开头匹配到结尾，整个字符串都要符合
print(bool(re.fullmatch(pattern, '第1章 ')))