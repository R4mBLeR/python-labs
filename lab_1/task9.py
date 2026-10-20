data_units = {"б": 1, "кб": 1024, "мб": 1024**2, "гб": 1024**3, "тб": 1024**4}
mass_units = {"мг": 0.001, "г": 1, "кг": 1000, "т": 1_000_000}
distance_units = {"мм": 0.001, "см": 0.01, "м": 1, "км": 1000}

all_categories = {
    "Данные": data_units,
    "Масса": mass_units,
    "Расстояние": distance_units,
}

unit_to_category = {}

for category_name, units in all_categories.items():
    for unit in units:
        unit_to_category[unit] = category_name

input_unit = input("Из какой единицы: ").strip().lower()
category_name = unit_to_category.get(input_unit)

if category_name is None:
    print(f"Неизвестная единица: '{input_unit}'")
else:
    units = all_categories[category_name]
    print(f"Категория: {category_name}")
    print(f"Доступные единицы: {','.join(units)}")

    value = float(input("Введите значение: "))
    output_unit = input("В какую единицу: ").strip().lower()

    if output_unit in units:
        result = value * units[input_unit] / units[output_unit]
        print(f"Результат: {result} {output_unit}")
    else:
        print(f"'{output_unit}' не относится к категории «{category_name}».")