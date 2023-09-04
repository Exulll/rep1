import csv
# from random import randint
# from datetime import datetime, timedelta
#
#
# def registration():
#     data = input('Имя, Фамилия, Отчество, др, логин, пароль: ').split()
#     passport = randint(1000000000, 9999999999)
#     data.insert(3, str(passport))
#     numb = acc_numb()
#     data.append(numb)
#     user = data[5]
#     card_data = card_creating(user)
#     data.extend(card_data)
#     data.append('0')
#     with open('bank.csv', 'a', encoding='utf8', newline='') as file1:
#         writer1 = csv.writer(file1)
#         writer1.writerow(data)
#
#
# def card_creating(user):
#     balance = str(randint(10000, 5000000))
#     card_number = str(randint(1000000000000000, 9999999999999999))
#     card_term = str(randint(1, 12)).zfill(2) + str(randint(2024, 2029))
#     cvc = str(randint(100, 999))
#     return balance, card_number, card_term, cvc
#
#
# def login():
#     logining = input('Введите логин: ')
#     password = input('Введите пароль: ')
#     with open('bank.csv', 'r', encoding='utf-8') as csvfile:
#         reader = csv.reader(csvfile)
#         for row in reader:
#             if row[5] == logining and row[6] == password:
#                 print('Вы вошли в систему')
#                 return
#         print('Неверный логин или пароль')
#
#
# def acc_numb():
#     prefix = 'S-'
#     suffix = randint(100000000, 999999999)
#     numbnumb = prefix + str(suffix)
#     return numbnumb
#
#
# def user_delete():
#     user = input("Введите ваш логин: ")
#     user_to_delete = input("Введите логин пользователя для удаления: ")
#
#     with open('bank.csv', 'r', encoding='utf8') as users:
#         reader = csv.reader(users)
#         user_list = list(reader)
#
#     logins = [row[5] for row in user_list[1:]]
#
#     if user in logins and user_to_delete in logins:
#         user_index = logins.index(user) + 1
#
#         if user_list[user_index][12] == '1':
#             with open('bank_updated.csv', 'w', newline='', encoding='utf8') as updated_users:
#                 writer = csv.writer(updated_users)
#
#                 for row in user_list:
#                     if row[5] != user_to_delete:
#                         writer.writerow(row)
#
#             print(f"Пользователь с логином '{user_to_delete}' успешно удален.")
#         else:
#             print("У вас нет доступа к удалению пользователей.")
#     elif user not in logins:
#         print(f"Текущий пользователь с логином '{user}' не найден.")
#     else:
#         print(f"Пользователь с логином '{user_to_delete}' не найден.")
#
#
# def card_info_func():
#     with open('bank.csv', 'r', encoding='utf8') as card_info:
#         reader = csv.reader(card_info)
#         ls = input('Введите номер счета: ')
#
#         found = False
#         for row in reader:
#             if row[7] == ls:
#                 data = row[7:]
#                 print(data)
#                 found = True
#                 break
#
#         if not found:
#             print('Счет не найден.')
#
#
# def apply_for_credit():
#     has_credit_card = input("Есть ли у вас кредитная карта? (Да/Нет): ")
#     credit_amount = float(input("Какую сумму вы хотели бы взять в качестве кредита? "))
#     credit_period = int(input("На сколько месяцев вы хотели бы взять кредит? "))
#
#     if has_credit_card.lower() == "да":
#         credit_receiving_date = '2026-09-27'
#     else:
#         credit_card_number = str(randint(1000000000000000, 9999999999999999))
#         credit_receiving_date = str(randint(1, 12)).zfill(2) + str(randint(2024, 2029))
#         credit_card_cvv = str(randint(100, 999))
#         print("Спасибо! Ваша новая кредитная карта готова к использованию.")
#         print(f'Номер карты: {credit_card_number}, дата выдачи: {credit_receiving_date}, cvv: {credit_card_cvv}')
#
#     monthly_payment = round((credit_amount * (1 + 0.1)) / credit_period, 2)
#     total_repayment = round(credit_amount * (1 + 0.1), 2)
#
#     exp_date = datetime.strptime(credit_receiving_date, "%Y-%m-%d")
#     print("\nЧЕК-ЛИСТ ОПЛАТ:\n")
#     for i in range(1, credit_period + 1):
#         payment_due = monthly_payment
#         new_exp_date = exp_date + timedelta(days=30 * i)
#
#         print(f"Месяц {i}: оплатить {payment_due} рублей до {new_exp_date.strftime('%Y-%m-%d')}")
#
#     print(f"\nЕжемесячный платеж: {monthly_payment} рублей")
#     print(f"Общая сумма возврата: {total_repayment} рублей")
#
#
# def deposit():
#     value = int(input('Введите сумму вклада: '))
#     years = int(input('Введите срок: '))
#     for i in range(years):
#         value *= 1.1
#     print(f'Через {years} лет сумма вклада составит {value}')
#
#
#
# while True:
#     choice = input('Регистрация/вход/удаление/получение кредита/вклад: ')
#     if choice == '1':
#         registration()
#         continue
#     elif choice == '2':
#         login()
#         continue
#     elif choice == '3':
#         user_delete()
#         continue
#     elif choice == '4':
#         apply_for_credit()
#         continue
#     elif choice == '5':
#         deposit()
#         continue
#     else:
#         break


def reg2():
    data = input('Имя, Фамилия, логин, пароль: ').split()
    root = '0'
    data.append(root)
    header = ['Name', 'Surname', 'login', 'password', 'root']
    with open('regist2.csv', mode='r', encoding='utf8', newline='', ) as checkhead:
        reader = csv.reader(checkhead)
        rows = list(reader)
        if rows[0] == header:
            pass
        else:
            with open('regist2.csv', mode='w', encoding='utf8', newline='', ) as head:
                rows.insert(0, header)
                writer = csv.writer(head)
                for row in writer:
                    writer.writerow(row)
#
#     with open('regist2.csv', mode='a', encoding='utf8', newline='', ) as users:
#         writer = csv.writer(users)
#         writer.writerow(data)
def writing():
    with open('bloknot.txt', 'w', encoding='utf8') as write:
        write.write(input())


def reading():
    with open('bloknot.txt', 'r', encoding='utf8') as read:
        a = read.readlines()
        print(a)

