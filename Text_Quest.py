# Код 'Текстового квеста'
import json


# файл json, а именно чтение графа игры
with open('graph.json', 'r') as finf:
    graph = json.load(finf)

# Вступление
print("\nВ этой игре вам предстоит совершать тяжелейшие выборы, только от ваших жизненных ценностей зависит как закончится эта история.\nДля выбора действия вводите номер под которым оно записано.")

# Основной код, рекурсивная функция
def start_game(way, items):
    
# Изменение сохранения
    with open('save.txt', 'w') as fsave:
        fsave.write(f'{way} {",".join(i for i in items)}')
        
# Вывод текста
    print()
    print(graph[way]['text'])
    
# Проверка на окончание игры
    if len(graph[way]['to_go']) == 0:
        print('\nКонец.')
        return 0
    
# Добавление предметов
    items += graph[way]['you_can_get']
    
# Проверка на переходную вершину (та у которой только один путь)
    if len(graph[way]['to_go']) == 1:
        return start_game(graph[way]['to_go'][0], items)
    
# Проверка на условие, например, есть ключ или нет
    if len(graph[way]['condition']) != 0:
        if graph[way]['condition'][0] in items:
            return start_game(graph[way]['to_go'][1], items)
        else:
            return start_game(graph[way]['to_go'][0], items)
    
# Получение выбора действия от игрока и проверка на корректность выбора
    inn = input()
    while inn not in [str(i) for i in range(1, len(graph[way]['to_go']) + 1)]:
        inn = input('Нет такого варианта. Выберите из доступных: ')
    
# Изменение положения играка в графе игры, запуск функции снова
    way = graph[way]['to_go'][int(inn) - 1]
    return start_game(way, items)


# Начинающий код
again = '1'
while again == '1':
    
# Создание сохранения
    with open('save.txt', 'r') as f:
        data = f.read()

# Создание переменных
    way = data.split()[0]
    items = data.split()[1].split(',') if len(data.split()) > 1 else []

# Запуск рекурссивной функции
    start_game(way, items)
    
# Вопрос после прохождения: играть ли заново?
    again = input('Хотите начать заново?\n1) Да.\n2) Нет.')
    
# Переход на начальную вершину графа
    with open('save.txt', 'w') as f:
        f.write("1")
