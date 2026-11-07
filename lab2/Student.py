class Student:
    _next_id = 1

    def __init__(self, name: str, last_name: str):
        self.name = name
        self.last_name = last_name
        self.speciality: str | None = None
        self.disciplines: list[str] = []
        self.grades: dict[str, int] = {}
        self.semester: int = 1

        self.id = Student._next_id
        Student._next_id += 1

    def get_course(self):
        return self.course

    def add_discipline(self, discipline: str) -> None:
        discipline = discipline.lower()
        disciplines = self.get_disciplines_and_specs()
        for dis in disciplines:
            dis = dis.lower()
        if discipline not in disciplines:
            raise ValueError("Неизвестная дисциплина")
        if self.speciality not in disciplines[discipline]:
            raise ValueError(
                    f"Данная дисциплина не читается для специальности: {self.speciality}"
                )
        if discipline in self.disciplines:
            raise ValueError(f"Студент уже изучает дисциплину: {discipline}")
        self.disciplines.append(discipline)

    def remove_discipline(self, discipline: str) -> None:
        if discipline not in self.disciplines:
            raise ValueError(f"Студент не изучает дисциплину: {discipline}")
        self.disciplines.remove(discipline)
        self.grades.pop(discipline, None)

    def set_grade(self, discipline: str, grade: int) -> None:
        if discipline not in self.disciplines:
            raise ValueError(f"Студент не изучает дисциплину: {discipline}")
        if not (1 <= grade <= 10):         
            raise ValueError("Отметка должна быть от 1 до 10")
        self.grades[discipline] = grade