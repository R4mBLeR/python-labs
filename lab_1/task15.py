data = [
    {'name': 'Яблоки', 'price': 50, 'amount': 10},  
    {'name': 'Бананы', 'price': 30, 'amount': 20},  
    {'name': 'Апельсины', 'price': 80, 'amount': 5} 
]
# Добавляет новую позицию если нету, меняет данные есть есть ключ name
def add_item(name: str, price: int, amount: int):
    for item in data:
        if (item['name']==name):
            item['price'] = price
            item['amount'] = amount
            return
    data.append({'name': name, 'price': price, 'amount': amount} )
    

max_revenue = 0
max_revenue_item = ""
print(data)
add_item('Груши', 50, 30)
add_item('Яблоки', 50, 30)
print(data)

for item in data:
    revenue = item['price']*item['amount']
    print(f'Выручка с товара: {item['name']}: {revenue}')
    if revenue > max_revenue:
        max_revenue = revenue
        max_revenue_item = item['name']

print(f'Самая большая выручка: {max_revenue}, c товара {max_revenue_item}')
print(f'Количество уникальныъ наименований: {len(data)}')
