from studyGroup import StudyGroup
#import courseStorage

class Course:
    def __init__(self, course_name, student_count, subject):
        self.__course_name = course_name
        self.__study_groups = []
        self.__study_group_size = 0
        self.__students = student_count
        self.__subject = subject
        #courseStorage.add_course(self)

    # Setters
    def set_course_name(self, new_course_name):
        self.__course_name = new_course_name

    # Getters
    def get_course_name(self):
        return self.__course_name

    # Add study group
    def add_study_group(self, group_name):
        if not self.group_exists(group_name):
            group = StudyGroup(group_name, self.__course_name)
            self.__study_groups.append(group)
            study_group_storage.add_study_groups(group)  # Assuming this is a method to store the group
            self.__study_group_size += 1
            print(f"{group_name} has been added to {self.__course_name}.")
        else:
            print("Study group cannot be added")

    # Check if a group exists
    def group_exists(self, group_name):
        return any(group.get_group_name() == group_name for group in self.__study_groups)

    # Remove a study group
    def remove_group(self, group_name):
        index = next((i for i, group in enumerate(self.__study_groups) if group.get_group_name() == group_name), -1)
        if index != -1:
            print(f"{self.__study_groups[index].get_group_name()} has been removed from the course \"{self.__course_name}\".")
            self.__study_groups.pop(index)
        else:
            print(f"Group \"{group_name}\" not found in the course.")
