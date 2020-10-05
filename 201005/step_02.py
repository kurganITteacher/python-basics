# concrete_request = 'https://translate.google.com/?hl=ru#view=home&op=translate&sl=en&tl=ru&text=patronymic'
concrete_request = 'https://translate.google.com/?view=home&op=translate&sl=en&tl=ru&text=patronymic'
# parse GET data -> dict
correct_answer = {
    'view': 'home',
    'op': 'translate',
    'sl': 'en',
    'tl': 'ru',
    'text': 'patronymic',
}

# ...
# print(concrete_request)

answer = None



assert answer == correct_answer, 'bad parser!'
