import sys

# to contain -> container -> arrays
# to read -> reader

# [12, 15, 95, 55, 36]

# !!! all is object !!! OOP
# объекты (пользователь)
#     - атрибуты: свойства (id, name, login, password)
#     - методы: действия (edit, delete, create, input_data)

# snake_case
# My_var
# my_Var
# myVar -> cameCase (Java, JS)

# 'ya.ru' -> reference
my_var = [12, '15', 95.32, 55, True]  # var -> reference
print(my_var, type(my_var), id(my_var), sys.getsizeof(my_var))

my_var = 12
print(my_var, type(my_var), id(my_var), sys.getsizeof(my_var))

my_var = 12.5
print(my_var, type(my_var), id(my_var), sys.getsizeof(my_var))

my_var = '12.5'
print(my_var, type(my_var), id(my_var), sys.getsizeof(my_var))
