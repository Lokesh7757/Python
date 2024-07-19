class Student:
    def __init__(self, name, marks):
        self.marks = marks
        self.name = name
        print("Insert New Record")

s1 = Student("lokesh", 85)
print(s1.name, s1.marks)
s2 = Student("Khankari", 96)
print(s2.name, s2.marks)