class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'Имя: {self.name}, Фамилия: {self.surname}'


Konstantin = Person(
    name='Константин',
    surname='Консерватор'
)

Ivan = Person(
    name='Иван',
    surname='Иванов'
)

print(Konstantin.__str__())
print(Ivan.__str__())
