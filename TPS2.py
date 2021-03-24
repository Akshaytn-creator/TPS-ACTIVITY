class Student:
    def __init__(self):
        self.name = input("Enter your name")
        self.marks_list = []
        for subject in range(5):
            self.marks_list.append(
                int(input(f"Enter marks for subject {subject + 1}:\n")))
        self.marks_list_tuple = tuple(self.marks_list)

    def calculate_grade(self):
        self.total_marks = 0
        self.grade = ""
        for score in self.marks_list_tuple:
            self.total_marks += score
        average = self.total_marks / len(self.marks_list_tuple)

        if average >= 90:
            self.grade = "S"
        elif average >= 80:
            self.grade = "A"
        elif average >= 70:
            self.grade = "B"
        elif average >= 60:
            self.grade = "C"
        elif average < 60:
            self.grade = "F"

        print(
            f"{self.name} got {average} marks on average.\n and a grade of {self.grade}")


students = [Student() for x in range(2)]

for student in students:
    student.calculate_grade()
