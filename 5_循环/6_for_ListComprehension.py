# 列表推导式; 更简洁的从从一个 list 创建新的 list

num_list = [1, 2, 3, 4]

num_list2 = [item * item for item in num_list]
print(num_list2)
