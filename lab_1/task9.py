units = {
    "б": 1,
    "кб": 1024,
    "мб": 1024 * 1024,
    "гб": 1024 * 1024 * 1024
}
value = float(input("Введите значение: "))
input_unit = input("Из какой единицы (б, кб, мб, гб): ").lower()
output_unit = input("В какую единицу (б, кб, мб, гб): ").lower()

result = (value * units[input_unit]) / units[output_unit]

print("Результат:", result, output_unit)