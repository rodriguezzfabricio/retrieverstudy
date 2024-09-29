from course import Course

courses = []
course_amount = 0

def add_course(course):
    global course_amount
    if isinstance(course, Course):
        courses.append(course)
        course_amount += 1

def remove_course(course_name):
    global course_amount
    index = next((i for i, course in enumerate(courses) if course.get_course_name() == course_name), -1)
    if index != -1:
        courses.pop(index)
        course_amount -= 1

def find_course(course_name):
    index = next((i for i, course in enumerate(courses) if course.get_course_name() == course_name), -1)
    if index != -1:
        return courses[index]
    else:
        print(f"{course_name} does not exist.")
