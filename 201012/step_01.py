# DRY
# inheritance

class People:
    def __init__(self):
        self.name = None
        self.surname = None
        self.age = None
        self.address = None
        self.mail = None
        self.phone_number = None


# for Student parent class People => call .__init__() for parent => super() - parent method call
class Student(People):
    def __init__(self):
        super().__init__()  # creates parent attributes
        self.id_student = None
        self.group_number = None


# for Teacher parent class People => call .__init__() for parent
class Teacher(People):
    def __init__(self):
        super().__init__()
        self.patronymic = None
        self.group_curator = None


# class Student:
#     def __init__(self):
#         self.id_student = None
#         self.name = None
#         self.surname = None
#         self.age = None
#         self.address = None
#         self.mail = None
#         self.phone_number = None
#         self.group_number = None
#
#
# class Teacher:
#     def __init__(self):
#         self.name = None
#         self.surname = None
#         self.patronymic = None
#         self.age = None
#         self.address = None
#         self.mail = None
#         self.phone_number = None
#         self.group_curator = None


# class Student:
#     def __init__(self):
#         self.surname = None
#         self.name = None
#         self.patronymic = None
#         self.age = 19  # hardcode
#         self.birthday = None
#         self.group = None


# class StudyGroup:
#     def __init__(self):
#         self.number = None
#         self.progress = None
#         self.specialty = None
#         self.mark = None  # what is it?


# class College:
#     def __init__(self):
#         self.abbreviation = None
#         self.specialties = []
#         self.license = None


# class Exam:
#     def __init__(self):
#         self.subject = None
#         self.mark = None
#         self.teacher = None
#         self.student = None
#         self.datetime = None


# class StudyGroup:
#     def __init__(self):
#         self.number = None
#         self.number_of_students = None
#         self.specialty = None
#         self.curator = None


# class Group:
#     def __init__(self):
#         self.specialty = None
#         self.number_of_students = None
#         self.id_of_students = []
#         self.patronymic = None
#         self.curator = None
#         self.number = None


# class Examination:
#     def __init__(self):
#         self.teacher = None
#         self.discipline = None
#         self.mark = None
#         self.data = None
#         self.time_for_exam = None
#         self.gradebook = None
