import random
speech_1 = ['Коллеги ', 'В то же время ', 'Однако ', 'Тем не менее ', 'Следовательно ', 'Соответственно ',
            'Вместе с тем ', 'С другой стороны ']
speech_2 = ['парадигма цифровой экономики ', 'контекст геймификации ', 'диджитализация бизнес-процессов ',
            'прагматичный подход к облачным платформам ', 'совокупность сквозных технологий ',
            'программа прорывных исследований ', 'ускорение блокчейн-транзакций ', 'экспоненциальный рост Big Data ']
speech_3 = ['открывает новые возможности для ', 'выдвигает новые требования ', 'несет в себе риски ',
            'расширяет горизонты ', 'заставляет искать варианты ', 'не оставляет шанса для ', 'повышает вероятность ',
            'обостряет проблему ']
speech_4 = ['дальнейшего углубления ', 'бюджетного финансирования ', 'синергетического эффекта ',
            'компроментации конфиденциальных ', 'несанкционированной кастомизации ', 'нормативного регулирования ',
            'практического применения ']
speech_5 = ['знаний и компетенций ', 'непроверенных гипотез ', 'волатильных активов ', 'опасных экспериментов ',
            'государственно-частных партнеров ', 'цифровых следов граждан ', 'нежелательных последствий ',
            'случайных открытий ']
speech_length = 0
speech_limit = random.randrange(5, 11)
print("Сгенерировано фраз", speech_limit)
while speech_length in range(speech_limit):
    if speech_limit == 5:
        print(random.choice(speech_1) + random.choice(speech_2) + random.choice(speech_3) + random.choice(speech_4) +
              random.choice(speech_5))
        break
    if speech_limit == 6:
        print(random.choice(speech_1) + random.choice(speech_2) + random.choice(speech_3) + random.choice(speech_4) +
              random.choice(speech_5) + random.choice(speech_1))
        break
    if speech_limit == 7:
        print(random.choice(speech_1) + random.choice(speech_2) + random.choice(speech_3) + random.choice(speech_4) +
              random.choice(speech_5) + random.choice(speech_1) + random.choice(speech_2))
        break
    if speech_limit == 8:
        print(random.choice(speech_1) + random.choice(speech_2) + random.choice(speech_3) + random.choice(speech_4) +
              random.choice(speech_5) + random.choice(speech_1) + random.choice(speech_2) + random.choice(speech_3))
        break
    if speech_limit == 9:
        print(random.choice(speech_1) + random.choice(speech_2) + random.choice(speech_3) + random.choice(speech_4) +
              random.choice(speech_5) + random.choice(speech_1) + random.choice(speech_2) + random.choice(speech_3) +
              random.choice(speech_4))
        break
    if speech_limit == 10:
        print(random.choice(speech_1) + random.choice(speech_2) + random.choice(speech_3) + random.choice(speech_4) +
              random.choice(speech_5) + random.choice(speech_1) + random.choice(speech_2) + random.choice(speech_3) +
              random.choice(speech_4) + random.choice(speech_5))
        break
