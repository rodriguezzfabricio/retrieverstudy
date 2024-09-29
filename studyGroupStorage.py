from studyGroup import StudyGroup

study_groups = []
study_group_amount = 0

def add_study_groups(group):
    global study_group_amount
    if isinstance(group, StudyGroup):
        study_groups.append(group)
        study_group_amount += 1

def remove_study_group(group_name):
    global study_group_amount
    index = next((i for i, group in enumerate(study_groups) if group.get_group_name() == group_name), -1)
    if index != -1:
        study_groups.pop(index)
        study_group_amount -= 1

def find_study_group(group_name):
    index = next((i for i, group in enumerate(study_groups) if group.get_group_name() == group_name), -1)
    if index != -1:
        return study_groups[index]
    else:
        print(f"{group_name} does not exist.")
        return -1

def create_studyGroup(group_name, course_name):
    study_group = StudyGroup(group_name, course_name)
    add_study_groups(study_group)
