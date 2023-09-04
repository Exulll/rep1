# a = list(map(int, input().split()))
# z = int(input())
# c = []
#
#
# def z2(a):
#     number = 0
#     while number < len(a) + 1:
#         if number % z == 0:
#             c.append(number)
#         number += 1
#
#
# z2(a)
# with open('z18txt1.txt', 'w', encoding='utf8') as z4:
#     for i in c:
#         z4.write(str(i) + '\n')
# a = input().split()  # Ввод ключей
# b = input().split()  # Ввод значений
# c = dict(zip(a, b))  # Создания словаря
# for i, j in c.items():
#     print(i, j)  # Вывод словаря
# with open('z18txt1.txt', 'w', encoding='utf8') as z7:
#     for i in c.keys():
#         z7.write(i + '\n')  # Вывод ключей

a = {
    'u1': 200,
    'u2': 1000,
    'u3': 666,
    }
def balance(ch):
    print(f'Ваш баланс: {a[ch]} очков')
def transfer(sender, receiver, amount):
    if amount > a[sender]:
        print("Ошибка: недостаточно очков для перевода.")
    else:
        a[sender] -= amount
        a[receiver] += amount
        print(f"Перевод выполнен успешно. Пользователь {sender} перевел {amount} очков пользователю {receiver}.+'\n'")
        history(sender, receiver, amount)
def history(sender, reciever, amount):
    with open('history.txt', 'a', newline='', encoding='utf8') as file:
        file.write(f'Пользователь {sender} перевел пользователю {reciever} {amount} очков')
while True:
    choice = input()
    if choice == '1':
        user = input()
        balance(user)
    elif choice == '2':
        sender = input()
        reciever = input()
        amount = int(input())
        transfer(sender, reciever, amount)
        history(sender, reciever, amount)
    elif choice == '3':
        with open('history.txt', 'r', encoding='utf8') as file:
            k = file.read()
            print(k)

    elif choice == '4':
        break
