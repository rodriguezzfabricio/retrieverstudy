from study_group import StudyGroup

class Student:
    def __init__(self, name, year, major, student_id, password, email, username):
        self.__username = username
        self.__name = name
        self.__year = year
        self.__major = major
        self.__id = student_id
        self.__phone_number = None
        self.__email = email
        self.__study_groups = []
        self.__password = password

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_year(self, year):
        self.__year = year

    def set_major(self, major):
        self.__major = major

    def set_id(self, student_id):
        self.__id = student_id

    def set_phone_number(self, number):
        self.__phone_number = number

    def set_email(self, email):
        self.__email = email

    def set_password(self, password):
        self.__password = password

    def set_username(self, username):
        self.__username = username

    # Getters
    def get_name(self):
        return self.__name

    def get_year(self):
        return self.__year

    def get_major(self):
        return self.__major

    def get_id(self):
        return self.__id

    def get_phone_number(self):
        return self.__phone_number

    def get_password(self):
        return self.__password

    def get_email(self):
        return self.__email

    def get_username(self):
        return self.__username

    # Add Study Group
    def add_study_group(self, group):
        if isinstance(group, StudyGroup):
            if not self.group_exists(group.get_group_name()):
                self.__study_groups.append(group)
            else:
                print(f"Group {group.get_group_name()} already exists.")

    def group_exists(self, group_name):
        return any(group.get_group_name() == group_name for group in self.__study_groups)

    # Print Details
    def print_details(self):
        print(f"Name: {self.__name}, Year: {self.__year}, Major: {self.__major}, ID: {self.__id}")
