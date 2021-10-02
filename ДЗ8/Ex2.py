from bs4 import BeautifulSoup
import requests
url = 'https://store.steampowered.com/genre/Free%20to%20Play/'
result = requests.get(url)
soup = BeautifulSoup(result.text, 'lxml')
tags = []
quantity = []

for tag in soup.find_all('span', class_='tag_name'):
    tags.append(tag.text)

for num in soup.find_all('span', class_='tag_count'):
    quantity.append(num.text)

tags_quantity_dict = dict(zip(tags, quantity))
for key, value in tags_quantity_dict.items():
    print("{0}: {1}".format(key, value))
