import requests

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

header = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=header)
print(f"status code: {r.status_code}")

response_dict = r.json()

# 处理结果
print(response_dict.keys())
print(response_dict)
