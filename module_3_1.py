calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    string_tuple = (len(string), string.upper(), string.upper().lower())
    print(string_tuple)


def is_contains(string, list_to_search):
    line_matches = False
    string_list = ''
    for i in list_to_search:
        if string.upper() == i.upper():
            line_matches = True
            string_list = i
            break
    if line_matches:
        print(f'{string} это в списке {string_list}')
    else:
        print(f'{string} в списке нет')
    count_calls()


list_1 = ['Olga', 'Nikolay', 'Denis', 'Sasha']
is_contains('SAshA', list_1)
string_info('Please check the work')
is_contains('Oleg', list_1)
is_contains(input('Введите имя '), list_1)
string_info(input('Ввведите строку '))
print(f'Всего вызвано программ: {calls}')
