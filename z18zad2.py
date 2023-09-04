import csv
a = {
    'u1': {
        'очки': 1000,
        'предметы': 'книга',
        'цена': 200,
          },
    'u2': {
        'очки': 3000,
        'предметы': 'стол',
        'цена': 600,
          },
    'u3': {
        'очки': 12000,
        'предметы': 'кресло',
        'цена': 500,
          },
    }
def buying():
    while True:
        p1 = input('покупатель: ')
        p2 = input('Продавец: ')
        item = input('Предмет: ')
        cost = (a[p2]['цена'])
        buyer_points = (a[p1]['очки'])
        if buyer_points < cost:
            print(f'У пользователя {p1} недостаточно очков для покупки')
            # with open('history2.csv', 'a', newline='', encoding='utf8') as f:

        print(f'пользователь {p1} купил у пользователя {p2} {item} за {cost} очков')
        a[p1]['очки'] -= cost
        a[p2]['очки'] += cost
        with open('history2.csv', 'a', newline='', encoding='utf8') as f:
            row = [p1, p2, item, cost]
            writer = csv.writer(f)
            writer.writerow(row)
        choice = input('y/n: ')
        if choice.lower() != 'y':
            break
def print_transactions():
    with open('history2.csv', 'r', encoding='utf8') as f:
        reader = csv.reader(f)
        print('История операций:')
        for row in reader:
            print(row)
buying()
print_transactions()
