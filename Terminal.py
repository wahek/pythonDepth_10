from datetime import datetime
from pathlib import Path
import controler


class PlasticCard:
    history = []
    AMOUNT_MULTIPLE = 50
    PERCENT_OF_TAKE = 0.015
    TAX_LIMIT = 5_000_000
    TAX_RICH = 0.9
    TRIPLE_TAX = 0.97

    def __init__(self, name):
        self.__score = 0
        self.name = name
        print('Карта активирована')

    def get_score(self):
        return self.__score

    @controler.logger('history.json')
    @controler.valid_amount(AMOUNT_MULTIPLE)
    def fill(self, amount):
        """Пополнить баланс"""
        current_dict = {'name': self.name, 'balance': self.__score, 'operation': 'fill', 'amount': amount,
                        'datatime': str(datetime.now())}
        if amount % self.AMOUNT_MULTIPLE == 0:
            self.__score += amount
            current_dict.update(successful=True)
            print(f'Сейчас на счету: {self.get_score()}')
            return current_dict
        else:
            current_dict.update(successful=False)
            print(f'Сейчас на счету: {self.get_score()}')
            return current_dict

    @controler.logger('history.json')
    @controler.valid_amount(AMOUNT_MULTIPLE)
    def take(self, amount):
        """Снять деньги"""
        current_dict = {'name': self.name, 'balance': self.__score, 'operation': 'take', 'amount': amount,
                        'datatime': str(datetime.now())}
        if amount % self.AMOUNT_MULTIPLE == 0 and self.__score >= amount:
            self.__score -= amount
            current_dict.update(successful=True)
            print(f'Сейчас на счету: {self.get_score()}')
            return current_dict
        else:
            current_dict.update(successful=False)
            print(f'Сейчас на счету: {self.get_score()}')
            return current_dict

    @staticmethod
    def get_history(name):
        return controler.get_history(name)


# a = PlasticCard('kerwefge')
# a.fill(100)
# a.take(100)
# print(a.get_history('kerwefge'))
