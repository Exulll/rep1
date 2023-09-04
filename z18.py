from random import randint
# a = 'hello.txt'
# with open(a, 'r', encoding='utf8') as z1:
#     z = z1.readlines()
#     z2 = z[-2]
#     print(z2)


# with open('def.txt', 'r+', encoding='utf8') as z2:
#     a = input()
#     z2.write(a)
#     z21 = z2.readline()
#     z12 = z21[::-1]
#     print(z12)


# with open('def.txt', 'r+', encoding='utf8') as z3:
#     max_ = ''
#     for i in z3:
#         i = i.strip()
#         if len(i) > len(max_):
#             max_ = i
#     print(max_)


# with open('def.txt', 'r+', encoding='utf8') as z4:
#     content = z4.read()
#     lines_c = content.count('\n') + 1
#     words_c = len(content.split())
#     letters_c = sum(1 for i in content if i.isalpha())
# print(letters_c)
# print(lines_c)
# print(words_c)


# with open('def.txt', 'r+', encoding='utf8') as z5:
#     sum_ = 0
#     for i in z5:
#         numbers = i.split()
#         for number in numbers:
#             sum_ += int(number)
#     print(sum_)


# with open('def.txt', 'w', encoding='utf8') as z6:
#     for i in range(11):
#         a = (randint(0, 1000))
#         z6.write(str(a) + '\n')
# with open('def.txt', 'r', encoding='utf8') as z6:
#     sum_ = 0
#     for line in z6:
#         num = int(line.strip())
#         sum_ += num
# print(sum_)


# a = input().split()
# b = map(int, input().split())
# c = dict(zip(a, b))
# try:
#     with open('z7.txt', 'w', encoding='utf8') as z7:
#         for i, j in c.items():
#             z7.write(i + ':' + str(j) + '\n')
#         print('Запись проведена успешно')
# except Exception as e:
#     print('Запись не проведена, ошибка:', str(e))

a = []
for i in range(10):
    a.append(randint(0, 10))
with open('def.txt', 'w', encoding='utf8') as z8:
    z = 0
    while z < len(a):
        if a[z] % 2 == 0 and a[z] % 5 == 0:
            z8.write(str(a[z]) + ' ')
        z += 1
    print(a)
# a = [0, 3, 3, 10, 2, 0, 0, 7, 5, 8]
# z = 0
# while z < len(a):
#     if a[z] % 2 == 0 and a[z] % 5 == 0:
#         with open('def.txt', 'a') as z8:
#             z8.write(str(a[z]) + " ")
#     z += 1
