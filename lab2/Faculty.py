
from Department import Department
from Student import Student


class Faculty:

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

    def remove_student(self, id: int):
        if id not in self.students:
            raise KeyError("Неизвестный ID студента")
        self.students.pop(id)

    def add_discipline_to_student(self, student_id: int, discipline: str) -> None:
        if student_id not in self.students:
            raise KeyError("Неизвестный ID студента")
        student: Student = self.students[student_id]
        disciplines = self.get_disciplines()
        if discipline not in disciplines:
            raise ValueError("Неизвестная дисциплина")
        if student.speciality not in disciplines[discipline]:
            raise ValueError(f"Данная дисциплина не читается для специальности:{student.speciality}")
        if discipline in student.disciplines:
            raise ValueError("Студент уже изучает данную дисциплину")
        student.add_discipline(discipline)

    def get_disciplines_and_specs(self):
        disciplines: dict[str, list[str]] = {}
        for dep in self.departments:
            for name, specs in dep.disciplines.items():
                disciplines[name] = specs
        return disciplines

    def set_grade(self, student_id: int, discipline: str, grade: int) -> None:
        if student_id not in self.students:
            raise KeyError("Неизвестный ID студента")
        student: Student = self.students[student_id]

        disciplines = self.get_disciplines_and_specs()
        if discipline not in disciplines:
            raise ValueError("Неизвестная дисциплина")
        if student.speciality not in disciplines[discipline]:
            raise ValueError(
                f"Данная дисциплина не читается для специальности: {student.speciality}"
            )

        student.set_grade(discipline, grade)

    def add_discipline_to_student(self, student_id: int, discipline: str) -> None:
        if student_id not in self.students:
            raise KeyError("Неизвестный ID студента")
        student: Student = self.students[student_id]

        disciplines = self.get_disciplines_and_specs()
        if discipline not in disciplines:
            raise ValueError("Неизвестная дисциплина")
        if student.speciality not in disciplines[discipline]:
            raise ValueError(
                f"Данная дисциплина не читается для специальности: {student.speciality}"
            )

        student.add_discipline(discipline)

    def transfer_to_next_semester(self, student_id: int) -> None:
        if student_id not in self.students:
            raise KeyError("Неизвестный ID студента")
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
