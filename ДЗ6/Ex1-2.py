import pickle
shows = {'Секретные материалы': {'Жанр': 'фантастика', 'Рейтинг': 0.9}, 'Ведьмак': {'Жанр': 'фэнтази', 'Рейтинг': 0.95},
         'Клан Сопрано': {'Жанр': 'криминал', 'Рейтинг': '0.8'}, '24': {'Genre': 'драма', 'Rating': 0.75},
         'Черное зеркало': {'Жанр': 'фантастика', 'Рейтинг': 0.98}, 'Во все тяжкие': {'Жанр': 'криминал',
                                                                                      'Рейтинг': '0.85'},
         'Игра престолов': {'Жанр': 'фэнтази', 'Рейтинг': 0.87},
         'Карточный домик': {'Genre': 'драма', 'Rating': 0.82}, 'Рик и Морти': {'Жанр': 'фантастика', 'Рейтинг': 1}}


def get_avg(lst):
    return sum(lst) / len(lst)


# Задание №1
val_list = []
for val in shows.values():
    try:
        val_list.append(float(val['Рейтинг']))
    except KeyError:
        val_list.append(float(val['Rating']))
print(f'Средний рейтинг всех сериалов: {get_avg(val_list)}')


# Задание №2
def film_name():
    genre_name = str(input('Введите жанр: '))
    print('Название жанра: ', genre_name)
    film_counter = 0
    rating_list = []
    film_list = []
    for names in shows:
        try:
            if shows[f'{names}']['Жанр'] == f'{genre_name}':
                film_counter += 1
                film_list.append(names)
                try:
                    rating_list.append(float(shows[f'{names}']['Рейтинг']))
                except KeyError:
                    rating_list.append(float(shows[f'{names}']['Rating']))
            else:
                continue
        except KeyError:
            if shows[f'{names}']['Genre'] == f'{genre_name}':
                film_counter += 1
                film_list.append(names)
                try:
                    rating_list.append(float(shows[f'{names}']['Рейтинг']))
                except KeyError:
                    rating_list.append(float(shows[f'{names}']['Rating']))
            else:
                continue
    print(f'Количество сериалов в жанре {genre_name}: {film_counter}')
    print(f'Средний рейтинг сериалов в жанре {genre_name}: {get_avg(rating_list)}')
    final_dict = dict(zip(film_list, rating_list))
    print(final_dict)
    with open('ИМЯ_ЖАНРА.dat', 'wb') as pickle_out:
        pickle.dump(final_dict, pickle_out)
    print(f'Словарь сохранен в формате .dat: \n{pickle_out}')


film_name()
