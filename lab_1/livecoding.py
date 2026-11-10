#Фитнес трекер: пользователь вводит еду и каллории, вводит упражнения и каллории. Декоратор выводит сообщение о том, сколько желательно еще портатить каллорий, норма 2500. Итоги в файл

food = {}
fitness = {}


def checker(func):
    def wrapper(*args):
        result = func(*args)
        if result > 0:
            with open("output.txt", "a", encoding="utf8") as file:
                    file.write(f"Вам нужно потратить еще {result} ккал. \n")
        return result
    return wrapper

def input_food():
    n = int(input("Введите колво позиций еды: "))
    for i in range(n):
        f = input("Название еды: ")
        cal = int(input("Количество калорий: "))
        food[f] = cal

def input_fit():
    n = int(input("Введите колво упражнений: "))
    for i in range(n):
        f = input("Название упражнения: ")
        cal = int(input("Количество калорий: "))
        fitness[f] = cal

@checker
def calculate(base: int):
    sum1 = 0
    sum2 = 0
    with open("output.txt", "w", encoding="utf8") as file:
        file.write(" Получено каллорий: \n")
        for f, c in food.items():
            sum1 += c
            file.write(f"{f} : {c} ккал\n")
        file.write(f"Сумма: {sum1}\n")
        file.write("\nПотрачено каллорий: \n")
        for f, c in fitness.items():
            sum2 += c
            file.write(f"{f} : {c} ккал\n")
        file.write(f"Сумма: {sum2}\n")
        print(f"Рассчет сохранен в output.txt")

    return sum1 - sum2 - base

input_food()
input_fit()
calculate(2500)
