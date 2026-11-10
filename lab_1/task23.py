import math

income = float(input("Введите доход за месяц в рублях: "))

categories = ["Жилье", "Питание", "Транспорт", "Развлечения", "Прочее"]
expenses = {}

print("\nВведите расходы по категориям")
for cat in categories:
    expenses[cat] = float(input(f"{cat}: "))

total_expense = sum(expenses.values())
savings = income - total_expense
savings_rate = 0
if income > 0:
    savings_rate = savings / income * 100

print("\n" + "=" * 30)
print(f"Всего расходов: {total_expense:.2f} руб.")
print(f"Остаток: {savings:.2f} руб. ({savings_rate:.1f}% дохода)")

print("\nДоли расходов:")
if total_expense > 0:
    for cat, amount in expenses.items():
        pct = amount / total_expense * 100
        print(f"{cat}: {amount:.2f} руб. ({pct:.1f}%)")
else:
    print("Расходов нет.")

print("\nРекомендации:", end=" ")
if savings < 0:
    print("Расходы превышают доходы, сократите траты на развлечения.")
elif savings_rate < 20:
    print("Норма сбережений ниже нормы, попробуйте урезать второстепенные расходы.")
else:
    print("Отличный баланс.")

top_cat = max(expenses, key=expenses.get)
print(f"Главная статья расходов: {top_cat} ({expenses[top_cat]:.2f} руб.).")

print("\nПланирование крупной покупки")
goal_name = input("На что хотите накопить? ")
goal_cost = float(input("Сколько это стоит (руб)? "))

if savings > 0:
    months = math.ceil(goal_cost / savings)
    print(f"При текущих сбережениях вы накопите на {goal_name} за {months} мес.")
else:
    print(f"Вы не откладываете деньги, накопить на {goal_name} сейчас невозможно.")