data = [
    {'name': 'Яблоки', 'price': 50, 'amount': 10},  
    {'name': 'Бананы', 'price': 30, 'amount': 20},  
    {'name': 'Яблоки', 'price': 50, 'amount': 5},   
    {'name': 'Апельсины', 'price': 80, 'amount': 5} 
]
max_revenue = 0
max_revenue_item = ""
for item in data:
    revenue = item['price']*item['amount']
    print(f'Выручка с товара: {item['name']}: {revenue}')
    if revenue > max_revenue:
        max_revenue = revenue
        max_revenue_item = item['name']

print(f'Самая большая выручка: {max_revenue}, c товара {max_revenue_item}')
print(f'Количество уникальныъ наименований: {len(data)}')
