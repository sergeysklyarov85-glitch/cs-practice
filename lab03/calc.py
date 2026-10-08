a = float(input('Введите первое число: '))
z = input('Введите знак')
b = float(input('Введите второе число: '))

if z == '+':
    print(a + b)
if z == '-':
    print(a - b)
if z == '/':
    if b != 0:
        print(a / b)
    else:
        print('Здесь не делят на ноль')
if z == '*' :
    print(a * b)
else:
    print('Неверный знак операции')