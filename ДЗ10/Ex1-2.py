import re
animals = ['питон', 'питон', 'кит', 'собака', 'питон', 'кит', 'кошка', 'горилла', 'кит', 'кошка', 'жираф', 'леопард',
           'жираф', 'жираф', 'кошка', 'горилла', 'жираф', 'жираф', 'кошка', 'жираф', 'кошка', 'кошка', 'собака', 'кит',
           'жираф', 'леопард', 'жираф', 'собака', 'кит', 'кит', 'кит', 'жираф', 'собака', 'собака', 'кит', 'питон',
           'леопард', 'кошка', 'жираф', 'собака', 'кошка', 'жираф', 'кошка', 'собака', 'кит', 'леопард', 'леопард',
           'горилла', 'горилла', 'кит']

# Задание 1
animal_name_length = list(map(len, animals))
print(animal_name_length)

animals_name_length1 = [len(animals) for animals in animals]
print(animals_name_length1)

# Задание 2


def filter_animals(name):
    if name[0] == 'к' or name[0] == 'л':
        return True
    else:
        return False


animals1 = list(filter(filter_animals, animals))
print(animals1)
animals2 = [animals for animals in animals if animals[0] == 'к' or animals[0] == 'л']
# Объясните как правильно называть переменные в list comprehension
print(animals2)
animals3 = " ".join(map(str, animals))
result = re.findall(r'\b[к|л][а-я]+', animals3)
print(result)
