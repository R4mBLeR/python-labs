class Department:
    def __init__(self, name):
        self.name = name
        self.disciplines = dict()

    def get_disciplines(self):
        return self.disciplines

    def add_discipline(self, name, specialities):
        self.disciplines[name] = specialities
