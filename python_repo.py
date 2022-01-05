import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

r = requests.get(url)
print("Status code: ", r.status_code)

response_dic = r.json()
print("Total repositorios: ", response_dic['total_count'])

# Explora informações sobre os repositórios
repo_dicts = response_dic['items']

name, stars = [], []

for repo_dict in repo_dicts:
    name.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
# cria a visualização
my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)


chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = name
chart.add('', stars)
chart.render_to_file('python_repos.svg')
