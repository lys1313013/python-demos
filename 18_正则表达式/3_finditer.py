import re

# 查找所有非重叠匹配项
text = "123 456 789"
pattern = re.compile(r'\d+')
matches = pattern.finditer(text)
for match in matches:
    print(match.group())
