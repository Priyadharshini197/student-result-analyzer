class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks  # dictionary {subject: mark}

    def get_total(self):
        return sum(self.marks.values())

    def get_average(self):
        return self.get_total() / len(self.marks)

    def get_grade(self):
        avg = self.get_average()

        if avg >= 90:
            return 'A+'
        elif avg >= 80:
            return 'A'
        elif avg >= 70:
            return 'B'
        elif avg >= 60:
            return 'C'
        elif avg >= 50:
            return 'D'
        else:
            return 'F'

    def is_pass(self):
        return all(mark >= 40 for mark in self.marks.values())