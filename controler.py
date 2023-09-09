import json

__score = 0
history = []
AMOUNT_MULTIPLE = 50
PERCENT_OF_TAKE = 0.015
TAX_LIMIT = 5_000_000
TAX_RICH = 0.9
TRIPLE_TAX = 0.97


def get_score():
    global __score
    return round(__score, 2)


def set_score(a):
    global __score
    __score = round(a, 2)


def check_multiple(amount: float) -> bool:
    if not amount % AMOUNT_MULTIPLE:
        return True
    else:
        return False


def percent_of_take(amount: float) -> int | float:
    percent = amount * PERCENT_OF_TAKE
    if percent < 30:
        print('Минимальный размер налога 30')
        return 30
    elif percent > 600:
        print('Максимальный размер налога 600')
        return 600
    else:
        return round(percent, 2)


def check_take(score: int | float, amount) -> bool:
    return False if score < amount else True


def check_rich(score: int | float):
    if score > TAX_LIMIT:
        return True


def rich_tax():
    set_score(get_score() * TAX_RICH)


def get_history():
    return history


def set_history(operation: tuple):
    global history
    history.append(operation)


def valid_amount(mult):
    def valid(func):
        def wrapper(*args):
            f = func(*args)
            if f['successful']:
                print(f'операция {f["operation"]} на {args[1]} успешна выполнена')
                return f
            else:
                print(f'Ошибка, отмена операции, сумма не кратна {mult}')
                return f

        return wrapper

    return valid


def logger(filename):
    def deco(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)

            with open(filename, 'r+', encoding='UTF-8') as data:
                try:
                    all_data = json.load(data)
                except json.decoder.JSONDecodeError:
                    all_data = []
                all_data.append(res)
                data.seek(0)  # Перемещение указателя файла в начало
                json.dump(all_data, data, indent=4)
                data.truncate()  # Усечение

        return wrapper

    return deco
