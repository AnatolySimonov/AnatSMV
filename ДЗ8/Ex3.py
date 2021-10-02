from bs4 import BeautifulSoup
import requests
import re
url = 'https://store.steampowered.com/genre/Free%20to%20Play/'
result = requests.get(url)
soup = BeautifulSoup(result.text, 'lxml')

game_list = []
for game_name in soup.find_all('div', class_='tab_item_name'):
    game_list.append(game_name.text)
print(game_list)

game_tags_list = []
for games in soup.find_all('div', class_='tab_item_details'):
    each_game_tags = games.text
    result = re.findall(r'\b\w+\b', each_game_tags)
    if 'Free' in result:
        del result[result.index('Free'): result.index('Free') + 3]
        result.append('Free to Play')
    game_tags_list.append(result)
game_tag_dict = dict(zip(game_list, game_tags_list))
for key, value in game_tag_dict.items():
    print("{0}: {1}".format(key, value))
