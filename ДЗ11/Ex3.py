import random


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Student(Person):
    def __init__(self, name, surname):
        Person.__init__(self, name, surname)

    def printer(self, professor):
        return f'Студент: {self.name} {self.surname}, Курс: {professor.course_to_read}'

    def student_to_str(self):
        return self.name + ' ' + self.surname


class Professor(Person):
    def __init__(self, name, surname, course_to_read):
        Person.__init__(self, name, surname)
        self.course_to_read = course_to_read

    @staticmethod
    def test_students(student_list):
        test_list = []
        for i in range(len(student_list)):
            test_list.append(random.randint(0, 10))
        return test_list

    def __str__(self):
        return f'Преподаватель: {self.name} {self.surname} читает курс {self.course_to_read}'


Semen = Professor(
    name='Семен',
    surname='Семенов',
    course_to_read='ООП'
)
Konstantin = Student(
    name='Константин',
    surname='Консерватор'
)
Ivan = Student(
    name='Иван',
    surname='Иванов'
)
students_list = [Konstantin.student_to_str(), Ivan.student_to_str()]
first_test = Semen.test_students(students_list)
second_test = Semen.test_students(students_list)
print(Semen.__str__())
print(Ivan.printer(Semen))
print(dict(zip(students_list, first_test)))
print(dict(zip(students_list, second_test)))
