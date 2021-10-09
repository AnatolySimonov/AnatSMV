import pandas as pd
import re

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)
pd.set_option('max_rows', None)
galaxies = pd.read_csv('galaxies.txt', dtype='str', sep=',')

galaxies_list = galaxies.values.tolist()

galaxies_names_list = galaxies['Галактика'].tolist()

for i in range(len(galaxies_names_list)):
    name_to_check = galaxies_names_list[i]
    result = re.search('Рыбы|Пегас|Кит', name_to_check)
    result2 = re.search(r'\b[A-Za-z]+', name_to_check)
    result3 = re.search(r'\d+$', name_to_check)
    if result:
        print(name_to_check)
    if result2:
        print(name_to_check)
    if result3:
        print(name_to_check)


