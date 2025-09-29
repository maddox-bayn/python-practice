class University:
    def __init__(self, university_name) -> None:
        self.university_name=university_name
    def show_detail(self):
        print(f"i study at {self.university_name} university")
class Course(University):
    def __init__(self, uni_name, course_name="software") -> None:
        self.course_name=course_name
        super().__init__(uni_name)
    def show_detail(self):
        print(f"study {self.course_name} in {self.university_name}")
class Branch(University):
    def __init__(self, uni_name, branch_name) -> None:
        self.branch_name=branch_name
        super().__init__(uni_name)
    def show_detail(self):
        print(f"i attend {self.university_name} university, in {self.branch_name} branch")
class Student(Course, Branch):
    def __init__(self, uni_name, course_name, branch_name, student_name) -> None:
        self.student_name=student_name
        super().__init__(uni_name, course_name)
    def show_detail(self):
        print(f"i am {self.student_name}, i attend {self.university_name} studying {self.course_name} in {self.branch_name} brach")
class Falculty(Branch):
    def __init__(self, uni_name, branch_name, falculty_name) -> None:
        self.falculty_name=falculty_name
        super().__init__(uni_name, branch_name)
    def show_detail(self):
        print(f"my falculty is {self.falculty_name} in {self.branch_name} branch, at {self.university_name} university")
#student_1 = Falculty("califonia", "AI", "software")
#student_1.show_detail()
student_2=Student("califonia","Mechine learning engineering","software", "Maddox Bayn")
student_2.show_detail()