anya = {'Секретные материалы': 'фантастика', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
olya = {'Клан Сопрано': 'криминал', '24': 'драма', 'Во все тяжкие': 'криминал', 'Карточный домик': 'драма'}
nastya = {'Ведьмак': 'фэнтази', 'Игра престолов': 'фэнтази'}
sveta = {'Черное зеркало': 'фантастика', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
set_anya = set(anya)
set_olya = set(olya)
set_nastya = set(nastya)
set_sveta = set(sveta)
int_quantity1 = len(set(set_anya & set_olya))
int_quantity2 = len(set(set_anya & set_nastya))
int_quantity3 = len(set(set_anya & set_sveta))
int_max = max(int_quantity1, int_quantity2, int_quantity3)
if int_max is int_quantity1:
    print('У Ани больше всего общих любимых сериалов с Олей')
elif int_max is int_quantity2:
    print('У Ани больше всего общих любимых сериалов с Настей')
else:
    print('У Ани больше всего общих любимых сериалов со Светой')
