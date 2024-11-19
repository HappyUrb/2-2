first = (input('Первое число: '))
second = (input('Второе число: '))
third = (input('Третье число: '))
if first == second == third:
    print(first, second, third, sep='\n')
elif first == second or first == third or second == third:
    print(2)
elif not(first == second == third):
    print(0)