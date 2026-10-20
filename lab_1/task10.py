amount = int(input("Сумма покупки: "))
age = int(input('Введите возраст: '))
is_birthday = bool(input('У вас день рождения? (1 - да, 0 - нет) '))
is_vip = bool(input('Вы вип клиент? (1 - да, 0 - нет) '))
discount = 0
if(amount>1000):
    discount= discount + 0.1
    
if(age>=63):
    discount= discount + 0.05


if(is_birthday):
    discount= discount + 0.05

if(is_vip):
    discount= max(discount, 0.15)

print(f'Ваша скидка: {discount * 100}%')
print(f'Итого: {amount * (1-discount)}')
