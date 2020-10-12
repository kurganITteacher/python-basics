# inheritance

class People:
    def __init__(self):
        self.name = None
        self.surname = None
        self.age = None
        self.address = None
        self.mail = None
        self.phone_number = None

    def say_hello(self):
        # print('привет, меня зовут ', self.name, '!')
        print('hello, my name is', self.name, '!')


class Student(People):
    def __init__(self):
        super().__init__()
        self.id_student = None
        self.group_number = None

    def say_group(self):
        print('my group is', self.group_number)


class Teacher(People):
    def __init__(self):
        super().__init__()
        self.patronymic = None
        self.speciality = None

    def say_speciality(self):
        print('my speciality is', self.speciality)


class HeadTeacher(Teacher):
    def call_teachers(self):
        print('everybody, come here!')


student_1 = Student()
student_1.say_hello()
student_1.say_group()

student_2 = Student()
student_2.say_hello()
student_2.say_group()

teacher_1 = Teacher()
teacher_1.say_hello()
# teacher_1.say_group()
teacher_1.say_speciality()

# class hierarchy: People -> Teacher -> HeadTeacher
teacher_2 = HeadTeacher()
teacher_2.say_speciality()
teacher_2.call_teachers()

# Device -> Phone -> SmartPhone
# Device -> Computer -> NoteBook -> UltraBook
# Device -> Computer -> DeskTop -> miniPC
# Device -> Computer -> Monoblock
