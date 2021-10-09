class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'Имя: {self.name}, Фамилия: {self.surname}'


konstantin = Person(
    name='Константин',
    surname='Консерватор'
)

ivan = Person(
    name='Иван',
    surname='Иванов'
)

print(Konstantin.__str__())
print(Ivan.__str__())
