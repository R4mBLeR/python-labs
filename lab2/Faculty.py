
import functools

from Department import Department
from Student import Student


class Faculty:

    #Декораторы реально штука прикольная
    def check_id(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            student_id = kwargs.get("student_id")
            if student_id not in self.students:
                raise KeyError("Неизвестный ID студента")
            return func(*args, **kwargs)  
        return wrapper   

    def __init__(self, name):
        self.name = name
        self.students: dict[int, Student] = {}
        self.specialities = []
        self.departments: list[Department] = []

    def add_student(self, student: Student, speciality: str):
        if(speciality not in self.specialities):
            raise ValueError("Попытка зачислить на несуществующую специальность")
        student.speciality = speciality
        self.students[student.id] = student

    @check_id
    def remove_student(self, id: int):
        self.students.pop(id)

    @check_id
    def add_discipline_to_student(self, student_id: int, discipline: str) -> None:
            student: Student = self.students[student_id]
            student.add_discipline(discipline)

    @check_id
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

    @check_id
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


    @check_id
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

    def get_specialities(self):
        return self.specialities

    def add_speciality(self, speciality: str):
        self.specialities.append(speciality)

    def get_departments(self):
        return self.departments

    def add_department(self, departament: Department):
        self.departments.append(departament)

                

