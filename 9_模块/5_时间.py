import time
t = time.time()
print(t)
t = time.localtime()
print(t)
print(t.tm_year)

print(time.strftime('%Y-%m-%d %H:%M:%S', t))