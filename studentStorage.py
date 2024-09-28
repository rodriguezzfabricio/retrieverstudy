from student import Student

students = []
student_amount = 0

def add_student(student):
    global student_amount
    if isinstance(student, Student):
        students.append(student)
        student_amount += 1

def remove_student(student_name):
    global student_amount
    index = next((i for i, student in enumerate(students) if student.get_name() == student_name), -1)
    if index != -1:
        students.pop(index)
        student_amount -= 1

def find_student(student_name):
    index = next((i for i, student in enumerate(students) if student.get_name() == student_name), -1)
    if index != -1:
        return students[index]
    else:
        print(f"{student_name} does not exist.")
