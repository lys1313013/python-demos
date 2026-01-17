import requests
import plotly.express as px

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

header = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=header)
print(f"status code: {r.status_code}")

response_dict = r.json()

# 处理结果
repo_dicts = response_dict['items']
repo_names, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

    # 悬停文本
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# 可视化
title = "在Github上最受欢迎的python项目"
labels = {"x": "Repository", "y": "Stars"}
fig = px.bar(x=repo_names, y=stars, title=title, labels=labels, hover_name=hover_texts)
fig.show()
