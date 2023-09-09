def get_menu():
    return '''Выберете операцию:
    1: Пополнить
    2: Снять
    3: Показать историю
    4: Выйти\n'''


def print_score(score: int | float):
    return f'На счету: {score}'


def print_amount_take():
    return 'Введите сумму которую хотите снять: '


def print_amount_insert():
    return 'Введите сумму на которую хотите пополнить: '


def print_accept():
    print('Операция прошла успешно')


def print_incorrect():
    return 'Некорректная операция <ОТМЕНА>'


def print_tax(tax_of: str, tax: int | float):
    return f'Взят налог на {tax_of}, размер налога: {tax}%'
