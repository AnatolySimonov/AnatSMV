anya = {'Секретные материалы': 'фантастика', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
olya = {'Клан Сопрано': 'криминал', '24': 'драма', 'Во все тяжкие': 'криминал', 'Карточный домик': 'драма'}
nastya = {'Ведьмак': 'фэнтази', 'Игра престолов': 'фэнтази'}
sveta = {'Черное зеркало': 'фантастика', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
anya_value_set = set(anya.values())
olya_value_set = set(olya.values())
nastya_value_set = set(nastya.values())
sveta_value_set = set(sveta.values())


def intersection(a, b):
    dictionary_intersected = list(a & b)
    return dictionary_intersected


anya_nastya = (intersection(anya_value_set, nastya_value_set))
print('Общие жанры Ани и Насти:',)
for i in range(len(anya_nastya)):
    print(anya_nastya[i])
olya_sveta = (intersection(olya_value_set, sveta_value_set))
print('Общие жанры Оли и Светы:', end=' ')
for i in range(len(olya_sveta)):
    print(olya_sveta[i])
sveta_anya = (intersection(sveta_value_set, anya_value_set))
print('Общие жанры Светы и Ани:', end=' ')
for i in range(len(sveta_anya)):
    print(sveta_anya[i], end=', ')
