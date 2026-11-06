from Department import Department
from Faculty import Faculty


def main():
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
    print(f"Факультет: {faculty.name}")
   