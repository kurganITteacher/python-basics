# say = 'всем привет!'
say = 'вСеМ пРивЕт!'
print(say)
# print(dir(say))
print(say.islower())
print(say.isupper())

say_2 = say.upper()
print(say_2)

# say_3 = say_2.capitalize()
say_3 = say.capitalize()
print(say_3)

if say.endswith('!'):
    print('эмоционально сказано')
