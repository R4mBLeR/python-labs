str = input("Введите строку: ")
is_pal = str == str[::-1]
if(is_pal): 
    print('Это палиндром') 
else:
    print('Это не палиндром')