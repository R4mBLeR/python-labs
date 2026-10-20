amount = int(input("Введите сумму: "))

nominals = [100, 50, 10, 5, 2, 1]

for nominal in nominals:
    count = amount // nominal
    
    amount = amount % nominal
    
    if count > 0:
        if nominal >= 5:
            print(f"Купюр по {nominal} руб.: {count}")
        else:
            print(f"Монет по {nominal} руб.: {count}")
