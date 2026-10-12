text = input("Введите первый список: ")
str_numbers = text.split()
first_numbers = []
for number in str_numbers:
    first_numbers.append(int(number))
text = input("Введите второй список: ")
str_numbers = text.split()
second_numbers = []
for number in str_numbers:
    second_numbers.append(int(number))
print(first_numbers)
identical_numbers = []
first_unique_numbers = []
second_unique_numbers = []
for number in first_numbers:
    if number in second_numbers:
        identical_numbers.append(number)
    else:
        first_unique_numbers.append(number)
for number in second_numbers:
    if number not in first_numbers:
        second_unique_numbers.append(number)
print(f' Одинаковые числа: {identical_numbers}')
print(f'Уникальные числа из первого набора: {first_unique_numbers}')
print(f'Уникальные числа из второго набора: {second_unique_numbers}')
print(f'Числа из двух набор за исключений одинаковых: {first_unique_numbers + second_unique_numbers}')
