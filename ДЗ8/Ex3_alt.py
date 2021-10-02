from bs4 import BeautifulSoup
import requests
url = 'https://store.steampowered.com/genre/Free%20to%20Play/'
result = requests.get(url)
soup = BeautifulSoup(result.text, 'lxml')

game_list = []
for game_name in soup.find_all('div', class_='tab_item_name'):
    game_list.append(game_name.text)
print(game_list)

tag_list = []
for tag_name in soup.find_all('div', class_='tab_item_top_tags'):
    tag_list.append(tag_name.text)
print(tag_list)

game_tag_dict = dict(zip(game_list, tag_list))
for key, value in game_tag_dict.items():
    print("{0}: {1}".format(key, value))
