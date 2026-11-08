
import csv
import functools

from Department import Department
from Student import Student


class Faculty:

    #Декораторы реально штука прикольная
    def _check_student_id(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            if args:
                student_id = args[0]
            else:
                student_id = kwargs.get("student_id")
            if student_id not in self.students:
                raise KeyError("Неизвестный ID студента")
            return func(self, *args, **kwargs)
        return wrapper

    def __init__(self, name):
        self.name = name
        self.students: dict[int, Student] = {}
        self.specialities = []
        self.departments: list[Department] = []

    #Базовые методы

    def get_specialities(self):
        return self.specialities

    def add_speciality(self, speciality: str):
        self.specialities.append(speciality)

    def get_departments(self):
        return self.departments

    def get_disciplines_and_deps(self) -> dict:
        disciplines = {}
        for dep in self.departments:
            for name, specs in dep.disciplines.items():
                disciplines[name] = dep.name
        return disciplines


    def add_department(self, departament: Department):
        self.departments.append(departament)

    def add_student(self, student: Student, speciality: str):
        if(speciality not in self.specialities):
            raise ValueError("Попытка зачислить на несуществующую специальность")
        student.speciality = speciality
        self.students[student.id] = student

    #Методы интерфейса

    @_check_student_id
    def remove_student(self, id: int):
        self.students.pop(id)
        
    @_check_student_id
    def add_discipline_to_student(self, student_id: int, discipline: str) -> None:
        student: Student = self.students[student_id]

        all_disciplines = self.get_disciplines_and_specs()

        if discipline not in all_disciplines:
            raise ValueError(f"Неизвестная дисциплина: {discipline!r}")

        if student.speciality not in all_disciplines[discipline]:
            raise ValueError(
                f"Данная дисциплина не читается для специальности: {student.speciality}"
            )

        student.add_discipline(discipline)

    @_check_student_id
    def remove_discipline_from_student(self, student_id: int, discipline: str) -> None:
        student: Student = self.students[student_id]
        if discipline not in student.disciplines:
            raise ValueError("У студента нет такой дисциплины")
        student.remove_discipline(discipline)

    def get_disciplines_and_specs(self):
        disciplines: dict[str, list[str]] = {}
        for dep in self.departments:
            for name, specs in dep.disciplines.items():
                disciplines[name] = specs
        return disciplines

    @_check_student_id
    def set_grade(self, student_id: int, discipline: str, grade: int) -> None:
        student: Student = self.students[student_id]

        disciplines = self.get_disciplines_and_specs()
        if discipline not in disciplines:
            raise ValueError("Неизвестная дисциплина")
        if student.speciality not in disciplines[discipline]:
            raise ValueError(
                f"Данная дисциплина не читается для специальности: {student.speciality}"
            )

        student.set_grade(discipline, grade)


    @_check_student_id
    def transfer_to_next_semester(self, student_id: int) -> None:
        student: Student = self.students[student_id]

        if not student.disciplines:
            raise ValueError("Студент не изучает ни одной дисциплины")

        for discipline in student.disciplines:
            if discipline not in student.grades or student.grades[discipline] < 4:
                raise ValueError(
                    f"Студент не может быть переведён: дисциплина '{discipline}' не сдана"
                )

        student.semester += 1

    @_check_student_id
    def save_student_info_to_file(self, student_id: int, filename=None):
        student: Student = self.students[student_id]
        if filename == None:
            filename = "Student_" + student.id
        with open(f"{filename}.txt", "w", encoding="utf8") as f:

            f.write(f"Отчет о студенте\n")
            f.write(f"{student.name} {student.last_name}\n")
            f.write(f"Специальность: {student.speciality}\n")

            average_grade = student.get_average_grade()
            dep_disc_grages = {}
            disc_and_deps = self.get_disciplines_and_deps()
            for dis in student.disciplines:
                dep = disc_and_deps[dis]
                dep_disc_grages.setdefault(dep, {})[dis] = student.grades.get(dis) 
            if average_grade == None:
                average_grade = "Отсутсвует"
            f.write(f"Средний балл: {average_grade}\n")
            f.write(f"Оценки по кафедрам:\n")
            for dep, disc_grades in dep_disc_grages.items():
                f.write(f"{dep}:\n")
                for dis, grade in disc_grades.items():
                    f.write(f"  {dis}: {grade}\n")

    def save_students_info_to_csv(self, filename=None):
        if filename == None:
            filename = "output"
        data = [
            ["ID", "Имя", "Фамилия", "Специальность", "Средний балл"]
        ]

        for student in self.students.values():
            data.append([student.id, student.name, student.last_name, student.speciality, student.get_average_grade()])

        with open(f"{filename}.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(data)
                



    

                

