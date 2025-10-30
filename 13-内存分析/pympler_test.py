from pympler import muppy, summary

# 获取当前所有 Python 对象
all_objects = muppy.get_objects()

# 按类型汇总
summarized = summary.summarize(all_objects)

# 打印类似 jmap -histo 的输出
summary.print_(summarized)