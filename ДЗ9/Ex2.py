import pandas as pd
import re

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)
pd.set_option('max_rows', None)
galaxies = pd.read_csv('galaxies.txt', dtype='str', sep=',')
galaxies_list = galaxies['Галактика'].tolist()
names_list = []
index_list = []
distance_list = []
remark_list = []
# Ищет все совпадения в столбце 'Галактика', добавляет их в отдельный список
# Также ищет все индексы строк, где присутствуют совпадения

for i in range(len(galaxies_list)):
    name_to_check = galaxies_list[i]
    result = re.search('[Аа]+ндромед', name_to_check)
    if result:
        names_list.append(name_to_check)
        index_list.append(int(galaxies[galaxies['Галактика'] == f'{name_to_check}'].index.values))
# print(names_list)
# print(index_list)

for index in range(len(index_list)):
    distance = galaxies.loc[index_list[index], 'Расстояние от Земли млн св. лет']
    distance_list.append(distance)
    remark = galaxies.loc[index_list[index], 'Примечания']
    remark_list.append(remark)
# print(distance_list)
# print(remark_list)
final_list = []

for (galaxy_name, galaxy_distance, galaxy_remark) in zip(names_list, distance_list, remark_list):
    each_galaxy_dict = dict(Название=f'{galaxy_name}', Расстояние=f'{galaxy_distance}', Примечание=f'{galaxy_remark}')
    final_list.append(each_galaxy_dict)

for elem in range(len(final_list)):
    print(final_list[elem])
