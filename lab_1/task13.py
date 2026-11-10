text = input("Введите числа: ")
str_numbers = text.split()

numbers = []
for s in str_numbers:
    if "." in s:
        numbers.append(float(s))
    else:
        numbers.append(int(s))

unique_numbers = []
duplicates = []
even_numbers = []
odd_numbers = []
negative_numbers = []
float_numbers = []
sum_multiples_of_5 = 0
max_number = numbers[0]
min_number = numbers[0]

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
    elif num not in duplicates:
        duplicates.append(num)

    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

    if num < 0:
        negative_numbers.append(num)

    if type(num) == float:
        float_numbers.append(num)

    if num % 5 == 0:
        sum_multiples_of_5 += num

    if num > max_number:
        max_number = num
    if num < min_number:
        min_number = num

print(f"Уникальные числа: {unique_numbers}")
print(f"Повторяющиеся числа: {duplicates}")
print(f"Четные числа: {even_numbers}")
print(f"Нечетные числа: {odd_numbers}")
print(f"Отрицательные числа: {negative_numbers}")
print(f"Числа с плавающей точкой: {float_numbers}")
print(f"Сумма чисел, кратных 5: {sum_multiples_of_5}")
print(f"Самое большое число: {max_number}")
print(f"Самое маленькое число: {min_number}")