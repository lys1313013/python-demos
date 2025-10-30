import sys
import gc

def get_total_memory():
    total = 0
    for obj in gc.get_objects():
        try:
            total += sys.getsizeof(obj)
        except Exception:
            pass
    return total

print("当前内存占用（估算）:", get_total_memory(), "bytes")