import tracemalloc

tracemalloc.start()

memory_hog = []
def use_memory():
    # 分配大约 chunk_mb MB 的内存（每个字符约1字节，所以乘以 1024*1024）
    chunk_mb = 10
    for i in range(10):
        chunk = 'x' * (chunk_mb * 1024 * 1024)
        memory_hog.append(chunk)
use_memory()

# 获取内存快照
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("[ Top 10 内存分配 ]")
for stat in top_stats[:10]:
    print(stat)