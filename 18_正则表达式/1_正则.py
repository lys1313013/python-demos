import re

print(bool(re.search(r'^第[0-9]+章', "第1章sss")))
print(bool(re.search(r'^\d\.\d', "1.1")))
print(bool(re.match(r'\d+', "123abc")))
