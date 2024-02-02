from logger import print_data, input_data, change_data, del_data


def interface():
    print("Добрый день! Вы попали на специальный бот справочник от GeekBrains! \n1 - запись данных \n2 - вывод данных \n3 - изменение данных \n4 - удаление данных")
    command = int(input("Введите число: "))
    
    while command not in [1, 2, 3, 4]:
        print("Неправильный ввод")
        command = int(input("Введите число: "))
    
    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        change_data()
    else:
        del_data()