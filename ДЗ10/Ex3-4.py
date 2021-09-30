shows = {'Секретные материалы': 'фантастика', 'Ведьмак': 'фэнтази', 'Клан Сопрано': 'криминал', '24': 'драма',
         'Черное зеркало': 'фантастика', 'Во все тяжкие': 'криминал', 'Игра престолов': 'фэнтази',
         'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
ratings = {'Секретные материалы': 0.9, 'Ведьмак': 0.95, 'Клан Сопрано': 0.8, '24': 0.75, 'Черное зеркало': 0.98,
           'Во все тяжкие': 0.85, 'Игра престолов': 0.87, 'Карточный домик': 0.82, 'Рик и Морти': 1}

# Задание 3
shows1 = {key: value for key, value in shows.items() if (value == 'фантастика' or value == 'фэнтази')}
print(shows1)
shows2 = [keys for keys in shows1.keys()]
print(shows2)

# Задание 4


def merge_dict(dict1, dict2):
    for k, v in dict2.items():
        if dict1.get(k):
            dict1[k] = [dict1[k], v]
        else:
            dict1[k] = v
    return dict1


sr = {key: {'Жанр': shows.get(key) for value in shows.get(key)} for key in shows.keys()}
print(sr)
sr1 = {key: {'Рейтинг': ratings.get(key) for value in shows.get(key)} for key in shows.keys()}
print(sr1)
print(merge_dict(sr, sr1))

