minutes = int(input('Колво потраченных минут: '))
sms = int(input('Колво потраченных смс: '))
mbps = int(input('Колво потраченных мегабайт: '))

sum = 24.99
print(f'Базовая сумма тарификации: {sum}')
minutes = minutes - 60
sms = sms - 30
mbps = mbps - 1024
minutes_price = (minutes > 0) * minutes * 0.89
sms_price = (sms > 0) * sms * 0.59
mbps_price = (mbps > 0) * mbps * 0.79
if minutes_price> 0:
    print(f'Сумма за дополнительно потраченные минут: {minutes_price}')
if sms_price> 0:
    print(f'Сумма дополнительно потраченные смс: {sms_price}')
if mbps_price> 0:
    print(f'Сумма дополнительно потраченные мегабайты: {mbps_price}')
full_sum = sum + sms_price+ mbps_price+ minutes_price
fee = full_sum * 0.02
print(f'Налог: {fee:.2f}')
print(f'Общая сумма с НДС: {(fee + full_sum):.2f}')
