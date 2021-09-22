import random
import module_dz5


def get_avg(lst):
    return sum(lst)/len(lst)


def intersection(a, b):
    dictionary_intersected = list(a & b)
    return dictionary_intersected


def get_titles(dct, value):  # вывод сериалов по жанру
    return [title for title in dct if (dct[title] == value)]


def get_avg_rate():  # вывод среднего рейтинга выбранных сериалов (требуется ручное изменение titles_rate)
    ratings = {'Секретные материалы': 0.9, 'Ведьмак': 0.95, 'Клан Сопрано': 0.8, '24': 0.75, 'Черное зеркало': 0.98,
               'Во все тяжкие': 0.85, 'Игра престолов': 0.87, 'Карточный домик': 0.82,
               'Рик и Морти': 1}
    titles_rate = [ratings.get('24'), ratings.get('Карточный домик')]  # ratings.get('')]
    title_rate_avg = module_dz5.get_avg(titles_rate)
    return [title_rate_avg]


def get_avg_rate2():
    ratings = {'Секретные материалы': 0.9, 'Ведьмак': 0.95, 'Клан Сопрано': 0.8, '24': 0.75, 'Черное зеркало': 0.98,
               'Во все тяжкие': 0.85, 'Игра престолов': 0.87, 'Карточный домик': 0.82,
               'Рик и Морти': 1}
    titles_rate = [ratings.get('Клан Сопрано'), ratings.get('Во все тяжкие')]  # ratings.get('')]
    title_rate_avg = module_dz5.get_avg(titles_rate)
    return [title_rate_avg]


def get_random_avg_rate(dct):  # вывод среднего рейтинга для рандомного пула сериалов
    ratings_items = list(dct.items())
    ratings_items = random.sample(ratings_items, random.randint(1, 9))
    ratings_items_dict = (dict(ratings_items))
    print('Случайно выбранные сериалы:', ratings_items_dict)
    ratings_values = list(ratings_items_dict.values())
    random_avg_rate = get_avg(ratings_values)
    return [random_avg_rate]
