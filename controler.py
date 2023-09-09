import json


def valid_amount(mult):
    def valid(func):
        def wrapper(*args):
            f = func(*args)
            if f['successful']:
                print(f'операция {f["operation"]} на {args[1]} успешна выполнена')
                return f
            else:
                print(f'Ошибка, отмена операции, сумма не кратна {mult}, либо на счету недостаточно средств')
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
                    all_data = {res['name']: []}
                try:
                    all_data[res['name']].append(res)
                except KeyError:
                    all_data[res['name']] = [res]
                data.seek(0)  # Перемещение указателя файла в начало
                json.dump(all_data, data, indent=4)
                data.truncate()  # Усечение

        return wrapper

    return deco


def get_history(name):
    with open('history.json', 'r', encoding='UTF-8') as data:
        a = json.load(data)
        return a[name]

# print(get_history('Ivan'))
