from logger import print_data, input_data


def interface():
    print("Добрый день! Вы попали на специальный бот справочник от GeekBrains! \n1 - запись данных \n2 - вывод данных")
    command = int(input("Введите число: "))
    
    while command != 1 and command != 2:
        print("Неправильный ввод")
        command = int(input("Введите число: "))
    
    if command == 1:
        input_data()
    else:
        print_data()