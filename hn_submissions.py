import requests
from operator import itemgetter

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)
# Processa informações sobre cada artigo submetido
submission_ids = r.json()
submission_dicts = []

sub_id = submission_ids[:30]

for submission_id in sub_id:
    # Cria uma chamada de API separada para cada artigo submetido
    url = (f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id='+str(submission_id),
        'comments': response_dict.get('descendants', 0),
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts,
                          key=itemgetter('comments'),
                          reverse=True)
