import requests
from pprint import pprint
from datetime import datetime, date, timedelta

def stackoverflow_questions(teg):
    to_date = int(datetime.now().timestamp())
    from_date = int((datetime.now() - timedelta(days=2)).timestamp())
    total_requests = 0
    for page_ in range(1, 14):
        url = f'https://api.stackexchange.com/2.3/questions?page={page_}&fromdate={from_date}&todate={to_date}' \
              f'&order=desc&sort=activity&pagesize=100&tagged={teg}&site=stackoverflow'
        result_list = []
        response = requests.get(url).json()
        for item in response['items']:
            link = item.get('link')
            result_list.append(link)
        total_requests += len(result_list)
    pprint(f'Всего запросов: {total_requests}, {result_list}')
stackoverflow_questions(teg='Python')
#[items][tags]