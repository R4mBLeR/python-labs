from Department import Department
from Faculty import Faculty
from Student import Student

def print_menu():
    print()
    print("=" * 40)
    print("1. Показать всех студентов")
    print("2. Зачислить нового студента")
    print("3. Отчислить студента")
    print("4. Записать студента на дисциплину")
    print("5. Убрать студента от дисциплины")
    print("6. Выставить оценку")
    print("7. Перевести на следующий семестр")
    print("0. Выход")

def init_fac():
    faculty = Faculty("РФиКТ")

    cybersecurity = "Кибербезопасность"
    informatics = "Прикладная информатика"
    faculty.add_speciality(cybersecurity)
    faculty.add_speciality(informatics)

    dep_cyber = Department("Кафедра кибербезопасности и ИТ")
    dep_cyber.add_discipline("Основы кибербезопасности", [cybersecurity, informatics])
    dep_cyber.add_discipline("Криптографические методы защиты информации", [informatics])
    dep_cyber.add_discipline("Программирование на JAVA", [cybersecurity, informatics])
    faculty.add_department(dep_cyber)

    dep_saikm = Department("Кафедра системного анализа и ИКМ")
    dep_saikm.add_discipline("Теория вероятностей и математическая статистика",
                             [cybersecurity, informatics])
    dep_saikm.add_discipline("Интеллектуальный анализ данных", [informatics])
    faculty.add_department(dep_saikm)
    return faculty

def main():
    faculty = init_fac()

    while True:
        print_menu()
        choice = input("Выберите действие (0-8): ").strip()

        if choice == "0":
            print("Выход из программы.")
            break

        try:
            if choice == "1":
                print("\nСтуденты факультета:")
                if not faculty.students:
                    print("Студенты отсутвуют")
                for sid, st in faculty.students.items():
                    print(f"  ID: {sid} | {st.last_name} {st.name} | Спец: {st.speciality}")
                continue

            if choice == "2":
                print("\nДобавление нового студента:")
                name = input('Введите имя: ').strip()
                last_name = input('Введите фамилию: ').strip()
                speciality = input('Введите специальность: ').strip()
                student = Student(name, last_name)
                faculty.add_student(student, speciality)
                continue

            if choice == "3":
                print("\Удаление студента:")
                id = int(input('Введите айди студента: ').strip())
                faculty.remove_student(id)
                continue
        except (ValueError, KeyError) as e:
            print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()