import re
import secrets

marker_prefix = "<IMAGE_MARKER_"
marker_suffix = ">"
# 匹配 Markdown 图片语法的正则表达式 匹配格式如：![alt text](image_id)
marker_pattern = re.compile(r"!\[[\s\S]*?\]\(/[-_a-zA-Z0-9]+\)")
marker_dict = {}


def replacement(match):
    original_marker = match.group(0)
    random_id = secrets.token_hex(8)
    marker_id = f"{marker_prefix}{random_id}{marker_suffix}"
    marker_dict[marker_id] = {
        "original_marker": original_marker,
    }
    return marker_id

# 预编译用于匹配已替换占位符的正则表达式
marker_regex = re.compile(re.escape(marker_prefix) + r"([a-f0-9]{16})" + re.escape(marker_suffix))
text = """
这是第一个：![](/55380d6af4e111f098540242ac120007-65a039f2f4e111f080db0242ac120007_pftud9ctuK9x0pVK) ； 这是第二个：![文本2](/a-_Z19) 
"""
res = marker_pattern.sub(replacement, text)
print("结果：")
print(res)
print("字典：")
print(marker_dict)