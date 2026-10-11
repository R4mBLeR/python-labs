
password = input('Введите пароль: ')
def checkPassword(password : str):
    if len(password)<16:
        print('Пароль слишком короткий')
        return
    if password.isalnum():
        print('Пароль состоит только из букв и цифр')
        return
    print('Надежный пароль')

checkPassword(password)
