class Student:
    _next_id = 0

    def __init__(self, name: str, last_name: str, course: int, age: int):
        self.name = name
        self.last_name = last_name
        self.speciality: str | None = None
        self.course = course
        self.age = age
        self.disciplines: list[str] = []
        self.grades: dict[str, int] = {}
        self.semester: int = 1

        self.id = Student._next_id
        Student._next_id += 1

    def get_course(self):
        return self.course

    def add_discipline(self, discipline: str) -> None:
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