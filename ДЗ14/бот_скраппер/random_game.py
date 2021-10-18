import requests
from bs4 import BeautifulSoup
import json
from content_randomgame import content_type
from random import randint, randrange


def find_max_starter(max_starter=245):
    page_link_json = content_type['Лидеры продаж'].replace('+', f'{max_starter}')
    url = f'{page_link_json}'
    request = requests.get(url)
    data_page = request.content

    while json.loads(data_page):
        if json.loads(data_page)['results_html'] == '':
            return max_starter
        else:
            max_starter += 15
            return find_max_starter(max_starter)


def load_data(start):
    page_link_json = content_type['Лидеры продаж'].replace('+', f'{start}')
    url = f'{page_link_json}'
    request = requests.get(url)
    data = request.content

    if json.loads(data)['results_html'] != '':
        dict_content = json.loads(data)
        soup = BeautifulSoup(dict_content['results_html'], 'lxml')

        rand_game = randint(0, len(soup.find_all(class_='tab_item_name')))

        game_name = soup.find_all(class_='tab_item_name')[rand_game].text
        game_tags = soup.find_all(class_='tab_item_top_tags')[rand_game].text
        game_link = soup.find_all(class_='tab_item')[rand_game].get('href')
        game_img_link = soup.find_all('img')[rand_game].get('src')

        game_info_dict = dict(Название=f'{game_name}', Тэги=f'{game_tags}',
                              Ссылка=f'{game_link}', Картинка=f'{game_img_link}')
        return game_info_dict


def get_data():
    max_start = find_max_starter()
    return load_data(randrange(0, max_start, 15))
