text = input("Введите первый список: ")
first_numbers = set(map(int, text.split()))

text = input("Введите второй список: ")
second_numbers = set(map(int, text.split()))
identical_numbers = []
first_unique_numbers = []
second_unique_numbers = []
identical_numbers = first_numbers & second_numbers
first_unique_numbers = first_numbers - second_numbers
second_unique_numbers = second_numbers - first_numbers

print(f' Одинаковые числа: {identical_numbers}')
print(f'Уникальные числа из первого набора: {first_unique_numbers}')
print(f'Уникальные числа из второго набора: {second_unique_numbers}')
print(f'Числа из двух набор за исключений одинаковых: {first_unique_numbers ^ second_unique_numbers}')
