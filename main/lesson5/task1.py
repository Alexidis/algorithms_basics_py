# 1. Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и
# отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
from collections import defaultdict


def main():
    enterprises = defaultdict(float)
    annual_profit = 0
    enterprise_count = int(input('Ведите количество предприятий '))
    for _ in range(enterprise_count):
        title = input('Ведите название организации ')
        avg_profit = 0
        for i in range(1, 5):
            quart_profit = float(input(f'Ведите прибыль {i}-го квартала '))
            avg_profit += quart_profit
        enterprises[title] = avg_profit / 4
        annual_profit += enterprises[title]
    annual_profit /= enterprise_count
    for title, profit in enterprises.items():
        print(f'Предприяти {title} в среднем за год заработало {profit}')
    bad_enterprise = [k for k, v in enterprises.items() if v < annual_profit]
    good_enterprise = [k for k, v in enterprises.items() if v > annual_profit]
    print(f'Предприятия {bad_enterprise} работали хуже среднего')
    print(f'Предприятия {good_enterprise} работали лучше среднего')
