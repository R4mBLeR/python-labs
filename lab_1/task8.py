import random


value = random.randint(1,100)
while True:
    a = int(input('Введите число: '))
    if(a>value):
        print('Меньше')
    elif(a<value):
        print('Больше')
    else: 
        print('Вы угадали!')
        break