#Code
import json


with open('graph.json', 'r') as finf:
    graph = json.load(finf)

print("\nВ этой игре вам предстоит совершать тяжелейшие выборы, только от ваших жизненных ценностей зависит как закончится эта история.\nДля выбора действия вводите номер под которым оно записано.")


def start_game(way, items):
    with open('save.txt', 'w') as fsave:
        fsave.write(way)
    print()
    print(graph[way]['text'])
    if len(graph[way]['to_go']) == 0:
        print('\nКонец.')
        return 0
    items += graph[way]['you_can_get']
    if len(graph[way]['to_go']) == 1:
        return start_game(graph[way]['to_go'][0], items)
    if len(graph[way]['condition']) != 0:
        if graph[way]['condition'][0] in items:
            return start_game(graph[way]['to_go'][1], items)
        else:
            return start_game(graph[way]['to_go'][0], items)
    inn = input()
    while inn not in [str(i) for i in range(1, len(graph[way]['to_go']) + 1)]:
        inn = input('Нет такого варианта. Выберите из доступных: ')
    way = graph[way]['to_go'][int(inn) - 1]
    return start_game(way, items)

again = '1'
while again == '1':
    way = '1'
    items = []
    start_game(way, items)
    again = input('Хотите начать заново?\n1) Да.\n2) Нет.')
