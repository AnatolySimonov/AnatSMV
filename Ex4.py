# -----------------------------------------------------------
# Запускается через раз
# Ломается после нескольких ответов "нет" в конце цикла
# -----------------------------------------------------------
import random
shows = {'Секретные материалы': 'фантастика', 'Ведьмак': 'фэнтази', 'Клан Сопрано': 'криминал', '24': 'драма',
         'Черное зеркало': 'фантастика', 'Во все тяжкие': 'криминал', 'Игра престолов': 'фэнтази',
         'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
ratings = {'Секретные материалы': 0.9, 'Ведьмак': 0.95, 'Клан Сопрано': 0.8, '24': 0.75, 'Черное зеркало': 0.98,
           'Во все тяжкие': 0.85, 'Игра престолов': 0.87, 'Карточный домик': 0.82,
           'Рик и Морти': 1}


def get_key(dct, value):
    return [key for key in dct if (dct[key] == value)]


i = 0
min_rate = 0.85
science_fiction = (get_key(shows, 'фэнтази'))
shows_list = list(shows)
shows_list_values = list(shows.values())
print('Не интересующие Вас сериалы:', science_fiction, ', а также сериалы с рейтингом ниже', min_rate)
science_fiction_index = shows_list.index('Ведьмак')
science_fiction_index1 = shows_list.index('Игра престолов')
ratings_list = list(ratings)
ratings_list_values = list(ratings.values())
while i < 1:
    random_rate = random.choice(list(ratings.values()))
    while random_rate < 0.85:
        random_rate = random.choice(list(ratings.values()))
        # print('Случайный рейтинг', random_rate)
        continue
    else:
        rate_index = ratings_list_values.index(random_rate)
        while rate_index == science_fiction_index or rate_index == science_fiction_index1:
            rate_index = ratings_list_values.index(random_rate)
            # print('Индекс рейтинга', rate_index)
            continue
        else:
            print("Как насчет сериала", ratings_list[rate_index], "?")
            if rate_index != science_fiction_index and rate_index != science_fiction_index1:
                answer = input('Вы довольны выбранным сериалом?')
                if answer == "да":
                    print("Приятного просмотра!")
                    i = i + 1
                elif answer == 'нет':
                    print("Попробуем сначала")
                    continue
