
a = float(input('Первое число: '))
c = input('Знак: ')
# print(f'{a}+{b} =', a+b)
# print(f'{a}-{b} =', a-b)
# print(f'{a}*{b} =', a*b)
# print(f'{a}/{b} =', a/b)
# print(f'{a}//{b} =', a//b)
# print(f'{a}%{b} =', a%b)
# print(f'{a}**{b} =', a**b)
b = float(input('Второе число: '))
if c == '+':
   print(a+b)
elif c == '-':
    print(a-b)
elif c == '*':
    print(a*b)
elif c == '/':
    if b != 0:
       print(a/b)
    else:
        print('На ноль делить нельзя')
elif c == '**':
    print(a**b)
