# # inheritance
#
# class People:
#     def __init__(self):
#         self.name = None
#         self.surname = None
#         self.age = None
#         self.address = None
#         self.mail = None
#         self.phone_number = None
#
#
# # for Student parent class People => call .__init__() for parent => super() - parent method call
# class Student(People):
#     def __init__(self):
#         super().__init__()  # creates parent attributes
#         self.id_student = None
#         self.group_number = None
#
#
# # for Teacher parent class People => call .__init__() for parent
# class Teacher(People):
#     def __init__(self):
#         super().__init__()
#         self.patronymic = None
#         self.group_curator = None


class WaterElemental:
    def create_river(self):
        print('here is the river')


class FireElemental:
    def create_firewall(self):
        print('firewall created')


class EarthElemental:
    def create_earthquake(self):
        print('big earthquake happens')


# multi-inheritance
class SuperHero(WaterElemental, FireElemental, EarthElemental):
    pass


# classic inheritance
class SouthWaterElemental(WaterElemental):
    def create_waterfall(self):
        print('waterfall sounds')


super_hero_1 = SuperHero()
print(type(super_hero_1))
super_hero_1.create_river()
super_hero_1.create_firewall()
super_hero_1.create_earthquake()

water_elemental_1 = WaterElemental()
print(type(water_elemental_1))
water_elemental_1.create_river()
# water_elemental_1.create_firewall()

water_elemental_2 = SouthWaterElemental()
print(type(water_elemental_2))
water_elemental_2.create_river()
water_elemental_2.create_waterfall()
