import random


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'Имя: {self.name}, Фамилия: {self.surname}'


class Student(Person):
    def __init__(self, name, surname, group, test_score):
        Person.__init__(self, name, surname)
        self.group = group
        self.test_score = [test_score]

    def set_test_score(self, test_score2):
        self.test_score.append(test_score2)
        return self.test_score

    def __str__(self):
        return f'Имя: {self.name}, Фамилия: {self.surname}, Группа: {self.group},' \
               f' Оценки: {self.test_score}'


konstantin = Student(
    name='Константин',
    surname='Консерватор',
    group='ГР-01',
    test_score=random.randint(0, 10)
)

ivan = Student(
    name='Иван',
    surname='Иванов',
    group='ГР-02',
    test_score=random.randint(0, 10)
)

konstantin.set_test_score(random.randint(0, 10))
ivan.set_test_score(random.randint(0, 10))
print(konstantin.__str__())
print(ivan.__str__())


class Professor(Person):
    def __init__(self, name, surname, subject):
        Person.__init__(self, name, surname)
        self.subject = subject
        self.students = [name, surname]

    def test_student(self, students):
        students.set_test_score.append(random.randint(0, 10))
        print(students)

    def __str__(self):
        return f'Преподаватель: {self.name} {self.surname} читает курс {self.subject}'


semen = Professor(
    name='Семен',
    surname='Семенов',
    subject='ООП'
)
print(semen.__str__())
