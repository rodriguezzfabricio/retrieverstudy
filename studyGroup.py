from student import Student

class StudyGroup:
    max_size = 8

    def __init__(self, group_name, course_name):
        self.__group_name = group_name
        self.__course_name = course_name
        self.__students = []
        self.__group_size = 0

    # Setters
    def set_group_name(self, new_name):
        self.__group_name = new_name

    def set_class(self, new_course):
        self.__course_name = new_course

    # Getters
    def get_group_name(self):
        return self.__group_name

    def get_class(self):
        return self.__course_name

    # Add student
    def add_student(self, student):
        if isinstance(student, Student):
            if self.__group_size < StudyGroup.max_size:  # Ensure group size does not exceed max_size
                self.__students.append(student)
                self.__group_size += 1
                student.add_study_group(self)
                print(f"{student.get_name()} has been added to the group \"{self.__group_name}\".")
            else:
                print(f"Cannot add {student.get_name()}. Group \"{self.__group_name}\" is full.")
        else:
            print("Invalid student. Please provide a valid Student object.")

    # Remove student
    def remove_student(self, student_name):
        index = next((i for i, student in enumerate(self.__students) if student.get_name() == student_name), -1)
        if index != -1:
            print(f"{self.__students[index].get_name()} has been removed from the group \"{self.__group_name}\".")
            self.__students.pop(index)
            self.__group_size -= 1
        else:
            print(f"Student \"{student_name}\" not found in the group.")

    # Print group details
    def print_group_details(self):
        print(f"Course: {self.__course_name}")
        print(f"Study Group: {self.__group_name}")
        print("Members:")
        for student in self.__students:
            student.print_details()
