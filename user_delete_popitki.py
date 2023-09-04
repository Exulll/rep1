import csv
# def user_delete():
#     user = input("Введите ваш логин: ")
#     user_to_delete = input("Введите логин пользователя для удаления: ")
#
#     with open('bank.csv', 'r', encoding='utf8') as users:
#         reader = csv.reader(users)
#         next(reader)
#         logins = [row[5] for row in reader]
#
#     with open('bank.csv', 'r', encoding='utf8') as delete_users:
#         reader = csv.reader(delete_users)
#         next(reader)
#         if user in logins:
#             for row in reader:
#                 if row[11] == '1':
#                     if user_to_delete in logins:
#                         print('sdfef')


def user_delete():
    user = input("Введите ваш логин: ")
    user_to_delete = input("Введите логин пользователя для удаления: ")

    with open('bank.csv', 'r', encoding='utf8') as users:
        reader = csv.reader(users)
        user_list = list(reader)

    logins = [row[5] for row in user_list[1:]]
    print(logins)

    if user in logins and user_to_delete in logins:
        user_index = logins.index(user) + 1

        if user_list[user_index][11] == '1':
            with open('bank_updated.csv', 'w', newline='', encoding='utf8') as updated_users:
                writer = csv.writer(updated_users)

                for row in user_list:
                    if row[5] != user_to_delete and row != user_list[user_index]:
                        writer.writerow(row)

            print(f"Пользователь с логином '{user_to_delete}' успешно удален.")
        else:
            print("У вас нет доступа к удалению пользователей.")
    elif user not in logins:
        print(f"Текущий пользователь с логином '{user}' не найден.")
    else:
        print(f"Пользователь с логином '{user_to_delete}' не найден.")
