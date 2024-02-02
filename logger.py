from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записывать даные? \n\n"
                    f"1 Вариант: \n"
                    f"{name}\n{surname}\n{phone}\n{address}\n\n"
                    f"2 Вариант: \n"
                    f"{name};{surname};{phone};{address}\n"
                    f"Выберите вариант: "))
    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input("Введите число: "))
    if var == 1:
        with open("data_first_variant.csv", 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    else:
        with open("data_second_variant.csv", 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n")
    
        
def print_data():
    print("Данные из первого файла:")
    with open("data_first_variant.csv", 'r', encoding='utf-8') as f:
            data_first = f.read().split("\n")
            for i in data_first:
                print(i)
    print("Данные из второго файла:")
    with open("data_second_variant.csv", 'r', encoding='utf-8') as f:
            data_second = f.read().split(";")
            print(" ".join(data_second))


def teg_change(data_dict):
    print("Выберите какую запить изменять: ")
    for i in data_dict:
        print(f"{i}:\n {' '.join(data_dict[i])}")

    num = int(input("Запись номер: "))
    if num in data_dict:
        for i in range(len(data_dict[num])):
            if data_dict[num][i] != '\n':
                print(f"Хотите изменить - {data_dict[num][i].strip()}?\n(Да, Нет)")
                if input() == 'Да':
                    data_dict[num][i] = input("Новое значение: ") + "\n"
    else:
        print("Такой записи нет, попробуйте заново")
    
    return data_dict


def enumerate_2_0(data):
    data_number = 0
    data_dict = {}
    for i in data:
        if i == "\n":
            data_number += 1
        elif data_number not in data_dict:
            data_dict[data_number] = [i]
        else:
            data_dict[data_number].append(i)
    return data_dict


def change_data():
    var = int(input(f"В каком файле поменять даные? \n"
                    f"1 Файл \n"
                    f"2 Файл \n"
                    f"Выберите вариант: "))
    
    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input("Введите число: "))
        
    if var == 1:
        with open("data_first_variant.csv", 'r', encoding='utf-8') as f:
            data_first = f.readlines()
            
            data_dict = enumerate_2_0(data_first)
            data_dict = teg_change(data_dict)

            with open("data_first_variant.csv", 'w', encoding='utf-8') as f:
                for i in data_dict:
                    data_dict[i].append("\n")
                    f.writelines(data_dict[i])
    
    else:
        with open("data_second_variant.csv", 'r', encoding='utf-8') as f:
            data_second = list(map(lambda x: x.split(";"), f.readlines()))
            data_dict = teg_change(dict(enumerate(data_second)))
            with open("data_second_variant.csv", 'w', encoding='utf-8') as f:
                for i in data_dict:
                    data_dict[i] = list(map(lambda x: x.strip(), data_dict[i]))
                    data_dict[i][-1] += '\n'
                    f.write(";".join(data_dict[i]))


def choise_del_data(data_dict):
    print("Выберите какую запить удалить: ")
    for i in data_dict:
        print(f"{i}:\n {' '.join(data_dict[i])}")
    num = int(input("Запись номер: "))
    while num not in data_dict:
        print("Неправильный ввод")
        num = int(input("Запись номер: "))
    return num

def del_data():
    var = int(input(f"В каком файле удалить даные? \n"
                    f"1 Файл \n"
                    f"2 Файл \n"
                    f"Выберите вариант: "))
    
    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input("Введите число: "))

    if var == 1:
        with open("data_first_variant.csv", 'r', encoding='utf-8') as f:
            data_first = f.readlines()
            data_dict = enumerate_2_0(data_first)
            
            num = choise_del_data(data_dict)
            del data_dict[num]
            with open("data_first_variant.csv", 'w', encoding='utf-8') as f:
                for i in data_dict:
                    data_dict[i].append("\n")
                    f.writelines(data_dict[i])
    else:
        with open("data_second_variant.csv", 'r', encoding='utf-8') as f:
            data_second = list(map(lambda x: x.split(";"), f.readlines()))  
            data_dict = dict(enumerate(data_second))  
            num = choise_del_data(data_dict)
            del data_dict[num]   
            with open("data_second_variant.csv", 'w', encoding='utf-8') as f:
                for i in data_dict:
                    data_dict[i] = list(map(lambda x: x.strip(), data_dict[i]))
                    data_dict[i][-1] += '\n'
                    f.write(";".join(data_dict[i]))

del_data()