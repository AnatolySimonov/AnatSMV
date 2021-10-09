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


semen = Professor(
    name='Семен',
    surname='Семенов',
    course_to_read='ООП'
)
konstantin = Student(
    name='Константин',
    surname='Консерватор'
)
ivan = Student(
    name='Иван',
    surname='Иванов'
)
students_list = [konstantin.student_to_str(), ivan.student_to_str()]
first_test = semen.test_students(students_list)
second_test = semen.test_students(students_list)
print(semen.__str__())
print(ivan.printer(semen))
print(dict(zip(students_list, first_test)))
print(dict(zip(students_list, second_test)))
