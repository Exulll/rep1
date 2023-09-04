a = {
    'черная': {
        'цена': 180,
        'количество': 1000,
              },
    'красная':  {
        'цена': 250,
        'количество': 500,
                },
    'фиолетовая': {
        'цена': 200,
        'количество': 800,
                   },
    'белая': {
        'цена': 150,
        'количество': 1200,
             },
    }
balance = 0


def buying():
    while True:
        global balance
        global a
        name = input('Имя покупателя: ')
        product = input('Предмет покупки: ').lower()
        count = int(input('Количество: '))
        price = count * a[product]['цена']
        if count > a[product]['количество']:
            print('Такого количества ткани нет на складе, уменьшите длину, либо выберите другую ткань')
            continue
        print(f'Вы купили {count} метров {product} ткани за {price}')
        with open('magazine.txt', 'a', encoding='utf8') as history:
            history.write(name + ': ' + str(price))
        balance += price
        a[product]['количество'] -= count
        choice = input()
        if choice != '1':
            break
        if balance > 100000:
            break
    choice2 = input()
    if choice2 == '1':
        with open('magazine.txt', 'r', encoding='utf8') as f:
            z = f.read()
            print(z)


buying()
print(balance)
