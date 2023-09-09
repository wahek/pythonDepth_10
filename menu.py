import os
import view
from Terminal import PlasticCard

clients = {}
try:
    os.remove('history.json')
    file = open('history.json', 'w')
    file.close()
except FileNotFoundError:
    file = open('history.json', 'w')
    file.close()


def operation(client):
    while True:
        match input(view.get_menu()):
            case '1':
                client.fill(int(input('Введите сумму')))
            case '2':
                client.take(int(input('Введите сумму')))
            case '3':
                print(PlasticCard.get_history(client.name))
            case '4':
                break
            case _:
                exit()


while True:
    current_client = input(view.sing_up())
    if current_client in clients:
        print(f'{current_client}, Вы вошли в систему')
        operation(clients[current_client])
    else:
        print('Добро пожаловать, новый пользователь')
        new_client = PlasticCard(current_client)
        clients[current_client] = new_client
        operation(new_client)
