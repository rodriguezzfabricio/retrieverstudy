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
        return -1

def login(email, password):
    student = None
    index = next((i for i, student in enumerate(students) if student.get_email() == email), -1)
    if index != -1:
        student = students[index]
    else:
        print(f"{student_name} does not exist.")
        return
    student_password = student.get_password()
    if password == student_password:
        return student
    else:
        print("Wrong Password")
        return

def sign_up(email, password, name, major, id, year):
    student = Student(name, year, major, id, password, email)
    add_student(student)
