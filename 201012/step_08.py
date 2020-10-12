# inheritance

class People:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = None
        self.address = None
        self.mail = None
        self.phone_number = None

    def about_me(self):
        print('привет, меня зовут', self.first_name, self.last_name, '!')
        # print('hello, my name is', self.first_name, self.last_name, '!')


class Student(People):
    def __init__(self, first_name, last_name, group_number='№33'):
        super().__init__(first_name, last_name)
        self.id_student = None
        self.group_number = group_number

    def say_group(self):
        print('группа', self.group_number)


class Teacher(People):
    def __init__(self, first_name, last_name, patronymic, speciality='учитель'):
        super().__init__(first_name, last_name)  # call parent init
        self.patronymic = patronymic
        self.speciality = speciality

    def say_speciality(self):
        print('моя специальность', self.speciality)

    def about_me(self):  # method override
        print('привет, я учитель, меня зовут', self.first_name, self.patronymic, self.last_name, '!')


class HeadTeacher(Teacher):
    def call_teachers(self):
        print('everybody, come here!')

    def about_me(self):
        print('привет, я завуч, меня зовут', self.first_name, self.patronymic, self.last_name, '!')


# # positional ARGumentS -> agrs
# student_1 = Student('Иван', 'Иванов', '№43')
# named arguments, Key Word ARGumentS -> kwargs
student_1 = Student('Иван', 'Иванов', group_number='№43')
student_1.about_me()
student_1.say_group()

# teacher_1 = Teacher(
#     speciality='математик', last_name='Петров', first_name='Петр', patronymic='Петрович'
# )
teacher_1 = Teacher(
    'Петр', 'Петров', speciality='математик', patronymic='Петрович'
)
teacher_1.about_me()
teacher_1.say_speciality()

teacher_2 = HeadTeacher('Эрнест', 'Сидоров', patronymic='Сергеевич')
teacher_2.about_me()
teacher_2.say_speciality()
teacher_2.call_teachers()
