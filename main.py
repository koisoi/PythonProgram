import sys

class Employee:                                                                                 # реализация класса "Сотрудник"
    class_name = "Сотрудник"
    employees = []

    def __init__(self, fullname, birthday, address, position, depts):
        while not (' ' in fullname.strip()):                                                    # валидация поля "ФИО"
            print("Поле \"ФИО\" должно содержать как минимум имя и фамилию сотрудника.")
            fullname = input("Введите новое имя: ")
        self.fullname = fullname
        
        while not ((birthday[2] == '.' and birthday[5] == '.') and (int(birthday[0:2]) <= 31) and       # валидация поля "Дата рождения"
                    (int(birthday[3:5]) <= 12) and (1900 <= int(birthday[6:10]) <= 2021)):
            print("Поле \"Дата рождения\" должно быть в формате ДД.ММ.ГГГГ и иметь верные числовые данные.")
            birthday = input("Введите новую дату рождения: ")
        self.birthday = birthday        
        
        self.address = address
        self.position = position
        self.depts = []
        depts = depts.split(',')
        
        for dep in depts:                                                                       # проверка на существование введенных отделов
            for depart in Departament.departaments:
                if depart.name == dep:
                    self.depts.append(depart)                                                   # добавление отдела к списку отделов
                    depart.empl_num += 1                                                        # увеличение сотрудников отдела на 1
                    depart.empls.append(self)                                                   # добавление сотрудника к списку сотрудников отдела
                    break
                else:
                    print(f"Отдел с названием {dep} не найден.")

        Employee.employees.append(self)                                                         # добавление сотрудника к общему списку сотрудников
    
    def input():                                                                                # создание объекта класса с помощью ввода с клавиатуры
        flnm = input("Введите ФИО сотрудника: ")                                                # валидация поля "ФИО"
        while not (' ' in flnm.strip()):
            print("Поле \"ФИО\" должно содержать как минимум имя и фамилию сотрудника.")
            flnm = input("Введите новое имя: ")

        brtd = input("Введите дату рождения: ")
        while not ((brtd[2] == '.' and brtd[5] == '.') and (int(brtd[0:2]) <= 31) and             # валидация поля "Дата рождения"
                    (int(brtd[3:5]) <= 12) and (1900 <= int(brtd[6:10]) <= 2021)):
            print("Поле \"Дата рождения\" должно быть в формате ДД.ММ.ГГГГ и иметь верные числовые данные.")
            brtd = input("Введите новую дату рождения: ")     
        
        adr = input("Введите адрес проживания: ")
        pos = input("Введите должность: ")
        depts = input("Через запятую введите отделы, к которым принадлежит сотрудник: ")   

        temp = Employee(flnm, brtd, adr, pos, depts)
        return temp

    def print(self):                                                                            # вывод информации о сотруднике
        print(f"Имя сотрудника: {self.fullname}")
        print(f"Дата рождения: {self.birthday}")
        print(f"Адрес проживания: {self.address}")
        print(f"Должность: {self.position}")
        print(f"Отделы:")
        for dep in self.depts:
            print(dep.name)

    def search():                                                                               # поиск записи о сотруднике по его ФИО
        name = input("Введите ФИО сотрудника: ")
        for empl in Employee.employees:
            if name == empl.fullname:
                print("Сотрудник найден. Информация о сотруднике:")
                empl.print()
                resp = input("Удалить сотрудника? y/n: ")
                if resp == "y":
                    empl.delete()
                return
        print("Сотрудник не найден.")

    def delete(self):                                                                           # удаление записи о сотруднике
        for i in range(len(Employee.employees)):                                                # удаление объекта из общего списка сотрудников
            if self == Employee.employees[i]:
                Employee.employees.pop(i)
        for dep in self.depts:                                                                  # удаление объекта из списка сотрудников отдела
            dep.empl_num -= 1
            for i in range(len(dep.empls)):
                if self == dep.empls[i]:
                    dep.empls.pop(i)
                    break
        print("Сотрудник успешно удален.")

    def __eq__(self, other):
        if (self.fullname == other.fullname) and (self.birthday == other.birthday) and (self.address == other.address) and (self.position == other.position) and (self.depts == other.depts):
            return True
        return False

class Departament:                                                                              # реализация класса "Сотрудник"
    class_name = "Отдел"
    departaments = []

    def __init__(self, name, rooms):
        self.name = name
        self.empl_num = 0
        self.rooms = rooms
        self.empls = []

        Departament.departaments.append(self)                                                   # добавление отдела в общий список отделов

    def input():                                                                                # создание объекта класса с помощью ввода с клавиатуры
        nm = input("Введите название отдела: ")
        rms = input("Укажите список комнат, в которых размещается отдел: ")

        temp = Departament(nm, rms)
        return temp

    def print(self):                                                                            # вывод информации об отделе
        print(f"Название отдела: {self.name}")
        print(f"Количество сотрудников: {self.empl_num}")
        print(f"Комнаты, в которых располагается отдел: {self.rooms}")

    def delete(self):                                                                           # удаление записи об отделе
        if self.empls:
                print("В этом отделе есть сотрудники, так что его невозможно удалить.")
                return
        for i in range(len(Departament.departaments)):                                          # удаление отдела из общего списка отделов
            if self == Departament.departaments[i]:
                Departament.departaments.pop(i)
                break
        print("Отдел успешно удален.")

    def search():                                                                               # поиск записи об отделе по его названию
        name = input("Введите название отдела: ")
        for dep in Departament.departaments:
            if name == dep.name:
                print("Отдел найден. Информация об отделе:")
                dep.print()
                resp = input("Хотите удалить отдел? y/n: ")
                if resp == "y":
                    dep.delete()
                return
        print("Отдел не найден.")

    def __eq__(self, other):
        if (self.name == other.name) and (self.empl_num == other.empl_num) and (self.rooms == other.rooms):
            return True
        return False

def main():                                                                                     # главная функция программы, реализует меню
    
    while True:
        print("Меню программы:")
        print()
        print("1. Добавить отдел")
        print("2. Найти отдел")
        print("3. Добавить сотрудника")
        print("4. Найти сотрудника")
        print("5. Выйти из программы")
        print()
        cmd = input("Введите команду: ")
        if cmd == "1":
            dep_temp = Departament.input()
            continue
        elif cmd == "2":
            Departament.search()
            continue
        elif cmd == "3":
            empl_temp = Employee.input()
            continue
        elif cmd == "4":
            Employee.search()
            continue
        elif cmd == "5":
            sys.exit(0)
        print("Введите только целое число от 1 до 5.")

if __name__ == "__main__":
    main()
