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
    print("8. Запись сведений о студенте в файл")
    print("9. Экспорт данных студентов в таблицу")
    print("0. Выход")

def init_fac():
    faculty = Faculty("РФиКТ")

    cybersecurity = "Кибербезопасность"
    informatics = "Прикладная информатика"
    faculty.add_speciality(cybersecurity)
    faculty.add_speciality(informatics)

    dep_cyber = Department("Кафедра кибербезопасности и информационных технологий")
    dep_cyber.add_discipline("Основы кибербезопасности", [cybersecurity, informatics])
    dep_cyber.add_discipline("Криптографические методы защиты информации", [informatics])
    dep_cyber.add_discipline("Программирование на JAVA", [cybersecurity, informatics])
    dep_cyber.add_discipline("Программирование микроконтроллеров", [cybersecurity])
    faculty.add_department(dep_cyber)

    dep_saikm = Department("Кафедра системного анализа и компьютерного моделирования")
    dep_saikm.add_discipline("Теория вероятностей и математическая статистика",
                             [cybersecurity, informatics])
    dep_saikm.add_discipline("Интеллектуальный анализ данных", [informatics])
    faculty.add_department(dep_saikm)

    ivan = Student("Иван", "Швецов")
    faculty.add_student(ivan, cybersecurity)
    id_ivan = ivan.id

    mikhail = Student("Михаил", "Радикевич")
    faculty.add_student(mikhail, informatics)
    id_mikhail = mikhail.id

    common = [
        "Основы кибербезопасности",
        "Программирование на JAVA",
        "Теория вероятностей и математическая статистика",
    ]
    for sid in (id_ivan, id_mikhail):
        for disc in common:
            faculty.add_discipline_to_student(sid, disc)

    faculty.add_discipline_to_student(id_ivan, "Программирование микроконтроллеров")
    for disc in ("Криптографические методы защиты информации",
                 "Интеллектуальный анализ данных"):
        faculty.add_discipline_to_student(id_mikhail, disc)

    ivan_grades = {
        "Основы кибербезопасности": 4,
        "Программирование на JAVA": 6,
        "Программирование микроконтроллеров": 10,
    }
    for disc, grade in ivan_grades.items():
        faculty.set_grade(id_ivan, disc, grade)

    mikhail_grades = {
        "Основы кибербезопасности": 4,
        "Программирование на JAVA": 8,
        "Теория вероятностей и математическая статистика": 10,
        "Криптографические методы защиты информации": 6,
        "Интеллектуальный анализ данных": 5,
    }
    for disc, grade in mikhail_grades.items():
        faculty.set_grade(id_mikhail, disc, grade)

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
                print("\nУдаление студента:")
                id = int(input('Введите айди студента: ').strip())
                faculty.remove_student(id)
                continue

            if choice == "4":
                print("\nЗачислить студента на курс")
                id = int(input('Введите айди студента: ').strip())
                discipline = input('Введите название дисциплины: ').strip()
                faculty.add_discipline_to_student(id, discipline)
                continue

            if choice == "5":
                print("\nтписать студента от курса")
                id = int(input('Введите айди студента: ').strip())
                discipline = input('Введите название дисциплины: ').strip()
                faculty.remove_discipline_from_student(id, discipline)
                continue

            if choice == "6":
                print("\nВыставить оценку за курс")
                id = int(input('Введите айди студента: ').strip())
                discipline = input('Введите название дисциплины: ').strip()
                grade = int(input('Введите оценку: ').strip())
                faculty.set_grade(id, discipline, grade)
                continue

            if choice == "7":
                print("\nПеревести на новый семестр")
                id = int(input('Введите айди студента: ').strip())
                faculty.transfer_to_next_semester(id)
                continue

            if choice == "8":
                print("\nЗапись сведений о студенте в файл")
                id = int(input('Введите айди студента: ').strip())
                filename = input('Введите имя файла: ').strip()
                faculty.save_student_info_to_file(id, filename)
                continue

            if choice == "9":
                print("\nЭкспорт данных студентов в таблицу")
                filename = input('Введите имя файла: ').strip()
                faculty.save_students_info_to_csv(filename)
                continue
            
        except (ValueError, KeyError) as e:
            print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()