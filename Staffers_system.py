
# Домашняя работа на 08.04.2023.

# Модуль 5. Файлы.
# Тема: Файлы. Часть 2


# Задание 1
# Напишите информационную систему «Сотрудники».
# Программа должна обеспечивать ввод данных, редактирование данных сотрудника, удаление сотрудника, поиск
# сотрудника по фамилии, вывод информации обо всех
# сотрудниках, указанного возраста, или фамилия которых
# начинается на указанную букву.
# Организуйте возможность
# сохранения найденной информации в файл. Также весь
# список сотрудников сохраняется в файл (при выходе из
# программы — автоматически, в процессе исполнения
# программы — по команде пользователя). При старте
# программы происходит загрузка списка сотрудников из
# указанного пользователем файла


# Решение (надеюсь поюзать систему будет интересно):

# Перед началом работы:
# 1. можно отдельно создать файл с расширением .txt и добавить в него тестовые строки,
# а затем открыть в программе.

# 2. можно ничего не создавать отдельно, а запустить код и вписать произвольное имя файла (без расширения)
# и пустой файл с расширением .txt создастся автоматически и будет отображаться как текущий в скобках над меню.

# Самое же приятное находится в поисковиках (4, 5, 6, 7): после того, как мы нашли требуемые данные в текущем файле,
# мы можем их не только СОХРАНИТЬ в сущетвующем файле (С ПЕРЕЗАПИСЬЮ - с утерей ранее записанных данных в этом файле),
# но и ДОПОЛНИТЬ сущетвующий файл этими данными (БЕЗ ПЕРЕЗАПИСИ - без утери уже имеющихся данных). Причем если этого
# файла ранее не существовало, то он будет создан автоматически.
# А также мы можем УДАЛЯТЬ эти найденные данные после того как их нашли и СОХРАНЯТЬ то, что от них осталось
# в любой другой файл.

# Во избежание недоразумений желательно ВНИМАТЕЛЬНО СЛЕДИТЬ ЗА ВВОДОМ!!!))

# Тестовые строки (копировать без #)
# {'ФИО': 'Рогов Ипполит Юлианович', 'Возраст': '50', 'Телефон': '+79846395798', 'Email': 'IURogov@mail.com', 'Должность': 'ведущий инженер', 'Зарплата': '100000', 'Кабинет': '10', 'Skype': 'Rogov090589'}
# {'ФИО': 'Князева Октябрина Федосеевна', 'Возраст': '48', 'Телефон': '+79973165846', 'Email': 'OFKnyazeva@mail.com', 'Должность': 'ведущий инженер', 'Зарплата': '100000', 'Кабинет': '12', 'Skype': 'Knyazeva15'}
# {'ФИО': 'Князева Октябрина Федосеевна', 'Возраст': '55', 'Телефон': '+79973165846', 'Email': 'OFKnyazva@mail.com', 'Должность': 'ведущий инженер', 'Зарплата': '100000','Кабинет': '12', 'Skype': 'Knyazeva15'}
# {'ФИО': 'Иванов Иван Иванович', 'Возраст': '50', 'Телефон': '+79846395792', 'Email': 'IIIvanov@mail.com', 'Должность': 'инженер', 'Кабинет': '6', 'Зарплата': '70000','Skype': 'Ivanov666'}

# создаём класс цветов результатов
class colors:
    # зелёный цвет
    G = '\033[92m'
    # красный цвет
    R = '\033[91m'
    # жёлтый цвет
    Y = '\033[93m'
    # голубой цвет
    B = '\033[96m'
    # сиреневый цвет
    L = '\033[95m'
    # синий цвет
    DB = '\033[94m'
    # серый цвет
    GR = '\033[90m'
    # окончание окрашивания
    ENDC = '\033[0m'

print()

# Функция записи данных в файл
def file_save(any_list, file_name):
    # Запись информации о всех сотрудниках в файл базы данных
    f_in = open(file_name, 'w', encoding='utf-8')
    # Построчная запись в файл базы данных информации по сотрудникам в формате словаря
    for item in any_list:
        f_in.write(str(item) + '\n')
    f_in.close()
    # Удаление пустых строк в файле
    with open(file_name, 'r', encoding='utf-8') as f_out:
        lines = f_out.readlines()
    lines = [line for line in lines if line.strip()]
    with open(file_name, 'w', encoding='utf-8') as f_in:
        f_in.writelines(lines)
    f_in.close()
    f_out.close()

# Функция чтения данных из файла
def file_read(file_name):
    import re
    import ast
    any_list1 = []
    f_out = open(file_name, 'r', encoding='utf-8')
    any_list = f_out.readlines()
    for i in range(len(any_list)):
        elem = eval(any_list[i])
        any_list1.append(elem)
    f_out.close()
    return any_list1

# Функция сохранения данных вручную
def manual_file_save(any_list, file_name):
    file_selection = input(f'СОХРАНИТЬ неизменённые данные ТОЛЬКО В ТЕКУЩИЙ файл {file_name} (С ПЕРЕЗАПИСЬЮ)? (1/0): ')
    if file_selection == '0':
        new_file_name = input('Введите имя нового файла: ')
        new_file_name += file_extension
        file_save(any_list, new_file_name)
        print('Сохранёние в новый файл базы данных (С ПЕРЕЗАПИСЬЮ) выполнено успешно!')
        print()
    elif file_selection == '1':
        file_save(any_list, file_name)
        print('Сохранение в первоначальный файл базы данных выполнено успешно!')
        print()

# Функция сохранения данных вручную для добавления найденных сотрудников в базу данных
def manual_file_save_with_add_to_new_file(any_list):
    file_name_add_to = input('Введите имя файла, который требуется ДОПОЛНИТЬ найденными данными (повторы сотрудников возможны): ')
    file_name_add_to += file_extension
    try:
        add_list = file_read(file_name_add_to)
    except (FileNotFoundError, UnicodeDecodeError):
        file_save(add_list, file_name_add_to)
        add_list = file_read(file_name_add_to)
        print()
    summ_list = any_list + add_list
    file_save(summ_list, file_name_add_to)
    print('Сохранёние в новый файл базы данных (БЕЗ ПЕРЕЗАПИСИ) выполнено успешно!')
    print()

# Функция сохранения данных вручную, предназначенная только для нюанса при добавлении сотрудника
def manual_file_save_for_add(any_list, new_any_list, any_dict, file_name, flag_save):
    if flag_save == '1':
        file_selection = input(f'СОХРАНИТЬ изменения в текущий файл {file_name}? (1/0): ')
        if file_selection == '0':
            new_file_name = input('Введите имя нового файла, в который сохранится только добавленный сотрудник: ')
            new_file_name += file_extension
            new_any_list.append(any_dict)
            file_save(new_any_list, new_file_name)
            print('Сохранёние в новый файл выполнено успешно!')
            print()
        elif file_selection == '1':
            any_list.append(any_dict)
            file_save(any_list, file_name)
            print('Сохранение в текущий файл выполнено успешно!')
            print()
    elif flag_save == '0':
        print('Выполнена ОТМЕНА сохранения!')
        print()

# Функция выбора удаления после того как сотрудники найдены
def delete_or_save():
    del_data = input(f'{colors.R}УДАЛИТЬ найденные данные из текущего файла? (1/0): {colors.ENDC}')
    if del_data == '0':
        save = input('СОХРАНИТЬ найденных сотрудников? (1/0): ')
        if save == '1':
            add_save = input('ДОПОЛНИТЬ данными (повторы сотрудников возможны) новый файл и сохранить ? (1/0): ')
            if add_save == '1':
                manual_file_save_with_add_to_new_file(search_list)
            elif add_save == '0':
                manual_file_save(search_list, database_file)
        elif save == '0':
            print('Выполнена ОТМЕНА сохранения!')
            print()
    elif del_data == '1':
        i = 0
        while i < len(search_list):
            j = 0
            while j < len(staffers_list):
                if search_list[i] == staffers_list[j]:
                    del staffers_list[j]
                else:
                    j += 1
            i += 1
        manual_file_save(staffers_list, database_file)

file_extension = '.txt'

# Приветствие
print()
print(f'{colors.Y}Вас приветствует информационная система "Сотрудник" ! {colors.ENDC}')
print()
print(f'{colors.R}(cистема работает с файлами с расширением {file_extension}, которое НЕ НУЖНО указывать в имени,')
print(f'{colors.R} т.к. оно присоединится к имени файла автоматически){colors.ENDC}')
print()
print()
database_file = input(f'{colors.G}Для дальнейшей работы введите имя файла: {colors.ENDC}')
database_file += file_extension
print()

try:
    staffers_list = file_read(database_file)
except (FileNotFoundError, UnicodeDecodeError):
    staffers_list = ['']
    file_save(staffers_list, database_file)
    staffers_list = file_read(database_file)
    print()

while True:
    print()
    print(f'{colors.DB}(текущий файл: {database_file}){colors.ENDC}')
    user_input = input(f'{colors.Y}Введите ваш запрос\n{colors.ENDC}'
                              f'{colors.G} 1. Добавить сотрудника\n{colors.ENDC}'
                              f'{colors.R} 2. Удалить сотрудника\n{colors.ENDC}'
                              f'{colors.R} 3. Изменить информацию о сотруднике\n{colors.ENDC}'
                              f'{colors.Y} 4. Найти сотрудника по ФИО (целиком с заглавных)\n{colors.ENDC}'
                              f'{colors.Y} 5. Найти сотрудника по возрасту\n{colors.ENDC}'
                              f'{colors.Y} 6. Найти сотрудника по первой букве фамилии\n{colors.ENDC}'
                              f'{colors.Y} 7. Показать всех сотрудников\n{colors.ENDC}'
                              f'{colors.R} 8. Открыть другой файл (использование существующего имени приведёт к стиранию данных в существующем файле)\n{colors.ENDC}'
                              f'{colors.R} 9. Создать новый файл без перехода в него (использование существующего имени приведёт к стиранию данных в существующем файле)\n{colors.ENDC}'
                             f'{colors.R}10. Создать новый файл с автопереходом в него (использование существующего имени приведёт к стиранию данных в существующем файле)\n{colors.ENDC}'
                              f'{colors.B} 0. Выход\n{colors.ENDC}'
                                f' : ')

    if user_input == '0':
        file_save(staffers_list, database_file)
        print()
        print(f'{colors.G}Перед выходом выполнено автосохранение в файл  {database_file}!{colors.ENDC}')
        print(f'{colors.Y}Выход из программы выполнен успешно!{colors.ENDC}')
        print()
        break

    if user_input == '1':
        # Добавление сотрудника в систему
        add_staffers_list = []
        name = input('Введите ФИО сотрудника: ')
        age = input('Введите возраст сотрудника: ')
        phone = input('Введите телефон сотрудника: ')
        email = input('Введите email сотрудника: ')
        position = input('Введите название должности сотрудника: ')
        salary = input('Введите зарплату сотрудника, руб.: ')
        room = input('Введите номер кабинета сотрудника: ')
        skype = input('Введите Skype сотрудника: ')
        staffer_dict = {'ФИО': name, 'Возраст': age, 'Телефон': phone, 'Email': email, 'Должность': position, 'Зарплата': salary, 'Кабинет': room, 'Skype': skype}
        print()
        save = input('СОХРАНИТЬ добавлененного сотрудника? (1/0): ')
        manual_file_save_for_add(staffers_list, add_staffers_list, staffer_dict, database_file, save)

    if user_input == '2':
        # Удаление сотрудника из системы
        name = input('ФИО удаляемого сотрудника: ')
        email = input(f'Удаляемый сотрудник {name} имеет email: ')
        len_staffers_list = len(staffers_list)
        new_staffers_list = []
        del_staffers_list = []
        print()
        for staff_dict in staffers_list:
            if staff_dict.get('Email') != email:
                new_staffers_list.append((staff_dict))
            else:
                del_staffers_list.append((staff_dict))
        for i in range(len(del_staffers_list)):
            print(f'{colors.R}{del_staffers_list[i]}{colors.ENDC}', end='\n')
        print()
        # print(staff_dict[email])
        staffers_list = []
        len_new_staffers_list = len(new_staffers_list)
        staffers_list = list(new_staffers_list)
        number_of_deleted = len_staffers_list - len_new_staffers_list
        print('Вышеуказанные данные удалены успешно!')
        print(f'Сотрудников, соответствующих запросу, найдено и удалено: {number_of_deleted}')
        print()
        file_save(staffers_list, database_file)
        print(f'После удаления выполнено автосохранение файла {database_file}!')
        print()

    if user_input == '3':
        # Замена данных сотрудника
        print("Введите ФИО и его e-mail сотрудника, информацию о котором нужно заменить:")
        name = input('ФИО сотрудника: ')
        email = input(f'{name} имеет email: ')
        len_staffers_list = len(staffers_list)
        new_staffers_list = []
        for i in range(len(staffers_list)):
            if staffers_list[i]['Email'] == email:
                staffers_list[i]
                print(f'{colors.G}{staff_dict}{colors.ENDC}')
                while True:
                    key = input("Введите название поля, которое нужно изменить,\n'"
                                "или введите * ддя выхода в главное меню: ")
                    if key == '*':
                        print("Вы вышли в главное меню")
                        break
                    if key in staffers_list[i]:
                        staffers_list[i][key] = input("Введите новое значение: ")
                        file_save(staffers_list, database_file)
                        print("Информация о сотруднике успешно обновлена и автоматически сохранена")
                        print()
                    else:
                        print("Неверное название поля")
                        print()

    if user_input == '4':
        # Поиск сотрудника по ФИО
        search_list = []
        count_search = 0
        name = input('ФИО искомого сотрудника: ')
        print()
        for staff_dict in staffers_list:
            if 'ФИО' in staff_dict.keys() and staff_dict['ФИО'] == name:
                print(f'{colors.G}{staff_dict}{colors.ENDC}')
                search_list.append(staff_dict)
                count_search += 1
        print()
        print(f'Сотрудников, соответствующих запросу, найдено: {count_search}')
        print()
        delete_or_save()
        del search_list

    if user_input == '5':
        # Поиск сотрудника по возрасту
        search_list = []
        count_search = 0
        age = input('Возраст искомого сотрудника: ')
        print()
        for staff_dict in staffers_list:
            if 'Возраст' in staff_dict.keys() and staff_dict['Возраст'] == age:
                print(f'{colors.G}{staff_dict}{colors.ENDC}')
                search_list.append(staff_dict)
                count_search += 1
        print()
        print(f'Сотрудников, соответствующих запросу, найдено: {count_search}')
        print()
        delete_or_save()
        del search_list

    if user_input == '6':
        # Поиск сотрудника по первой букве фамилии
        search_list = []
        count_search = 0
        first_letter = input('Первая буква фамилии искомого сотрудника: ')
        for i in range(len(staffers_list)):
            if ((staffers_list[i]['ФИО'].strip().split())[0])[0].lower() == first_letter.lower():
                search_list.append(staffers_list[i])
                count_search += 1
        print()
        for staff_dict in search_list:
            print(f'{colors.G}{staff_dict}{colors.ENDC}')
        print()
        print(f'Сотрудников, соответствующих запросу, найдено: {count_search}')
        print()
        delete_or_save()
        del search_list

    if user_input == '7':
        # Поиск всех сотрудников
        search_list = []
        count_search = 0
        print()
        for staff_dict in staffers_list:
            print(f'{colors.G}{staff_dict}{colors.ENDC}')
            search_list.append(staff_dict)
            count_search += 1
        print()
        print(f'Сотрудников, соответствующих запросу, найдено: {count_search}')
        print()
        delete_or_save()
        del search_list

    if user_input == '8':
        # Открытие другого файла
        file_save(staffers_list, database_file)
        database_file = input('Введите имя файла: ')
        database_file += file_extension
        print()
        try:
            staffers_list = file_read(database_file)
        except (FileNotFoundError, UnicodeDecodeError):
            file_save(staffers_list, database_file)
            staffers_list = file_read(database_file)
            print()

    if user_input == '9':
        # Создание нового файла
        file_save(staffers_list, database_file)
        new_database_file = input('Введите имя нового файла: ')
        new_database_file += file_extension
        staffers_list = []
        file_save(staffers_list, new_database_file)
        staffers_list = file_read(database_file)
        print()

    if user_input == '10':
        # Создание нового файла с переходом в него
        file_save(staffers_list, database_file)
        database_file = input('Введите имя нового файла: ')
        database_file += file_extension
        staffers_list = []
        file_save(staffers_list, database_file)
        staffers_list = file_read(database_file)
        print()