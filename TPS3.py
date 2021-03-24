class NotAlphaError(Exception):
    '''Raised when the string contains non-alphabets '''
    pass


class Student:
    def __init__(self):
        try:
            self.name = input("Enter your name")
            if not self.name.isalpha():
                raise NotAlphaError
        except NotAlphaError:
            print("NotAlphaError - Please enter only alphabets")
            exit()
        self.marks_list = []
        for subject in range(5):
            try:
                self.marks_list.append(
                    int(input(f"Enter marks for subject {subject + 1}:\n")))
            except ValueError:
                print("Value Error - Enter only numbers")
                exit()

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


try:
    n = int(input("Enter number of students in class:\n"))
except ValueError:
    print("ValueError, Please enter numbers only")
    exit()

try:
    students = [Student() for x in range(n)]
except NameError:
    print("NameError, undefined Variable")
    exit()

for student in students:
    student.calculate_grade()
