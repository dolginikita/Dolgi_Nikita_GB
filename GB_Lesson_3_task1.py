


def num_translate():
    number = input('Введите число на английском: ')
    print(numbers.get(number.lower()))


numbers = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'For': 'Четыре',
    'Five': 'Пять',
    'Six': 'Шесть',
    'Seven': 'Семь',
    'Eight': 'Восемь',
    'Nine': 'Девять',
    'Ten': 'Десять',
}

num_translate()