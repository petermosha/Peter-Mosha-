class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score


class Gradebook:
    def __init__(self):
        self.students = [] 

    def add_student(self, student):
        self.students.append(student)

    def get_average(self):
        if len(self.students) == 0:
            return 0

        total = 0
        for student in self.students:
            total += student.score

        return total / len(self.students)



gradebook = Gradebook()

s1 = Student("petermosha", 27)
s2 = Student("afrah", 45)
s3 = Student("landof", 20)

gradebook.add_student(s1)
gradebook.add_student(s2)
gradebook.add_student(s3)

print("Class Average:", gradebook.get_average())

