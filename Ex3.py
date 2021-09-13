shows = {'Секретные материалы': 'фантастика', 'Ведьмак': 'фэнтази', 'Клан Сопрано': 'криминал', '24': 'драма',
         'Черное зеркало': 'фантастика', 'Во все тяжкие': 'криминал', 'Игра престолов': 'фэнтази',
         'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
ratings = {'Секретные материалы': 0.9, 'Ведьмак': 0.95, 'Клан Сопрано': 0.8, '24': 0.75, 'Черное зеркало': 0.98,
           'Во все тяжкие': 0.85, 'Игра престолов': 0.87, 'Карточный домик': 0.82,
           'Рик и Мор ти': 1}


def get_key(dct, value):
    return [key for key in dct if (dct[key] == value)]


science_fiction = (get_key(shows, 'фантастика'))
sf_length = len(science_fiction)
ratings_list = list(ratings)
index1 = ratings_list.index('Секретные материалы')
index2 = ratings_list.index('Черное зеркало')
index3 = ratings_list.index('Рик и Морти')
print('Рейтинг сериала "Секретные материалы": ', ratings.get(ratings_list[index1]))
print('Рейтинг сериала "Черное зеркало": ', ratings.get(ratings_list[index2]))
print('Рейтинг сериала "Рик и Морти": ', ratings.get(ratings_list[index3]))
avg_rate = (ratings.get(ratings_list[index1]) + ratings.get(ratings_list[index2])
            + ratings.get(ratings_list[index3])) / 3
print('Средний рейтинг сериалов жанра "Фантастика":', avg_rate)



