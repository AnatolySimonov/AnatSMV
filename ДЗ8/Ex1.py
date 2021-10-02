from bs4 import BeautifulSoup
import requests
import re
url = 'https://store.steampowered.com/genre/Free%20to%20Play/'
result = requests.get(url)
soup = BeautifulSoup(result.text, 'lxml')
ftp_list = []
url_list = []

for link in soup.find_all('a'):
    link_text = link.text
    link_url = link.get('href')
    pattern = re.compile('Free To Play')
    result1 = pattern.findall(link_text)
    for i in range(len(result1)):
        if result1:
            ftp_list.append(result1[i])
            url_list.append(link_url)

link_dict = {k: v for k in url_list for v in ftp_list}
for key, value in link_dict.items():
    print("{0}: {1}".format(key, value))
