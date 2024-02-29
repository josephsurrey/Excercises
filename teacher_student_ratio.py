import easygui as eg


def get_info():
    school_name = eg.enterbox("Enter the name of the school:", "School Name")
    maximum_class_size = eg.integerbox("What is the max number of students per class?\n"
                                       "Must be a number between 10 and 30", "Maximum Class Size",
                                       25, 10, 30)
    total_students = eg.integerbox(f"What is the total number of children at {school_name}?\n"
                                   f"Must be a number between 10 and 1400", "Total Number of Students",
                                   800, 10, 1400)
    teachers = eg.integerbox(f"What is the number of teachers at {school_name}?\n"
                             f"Must be a number between 1 and 120", "Number of Teachers",
                             10, 1, 120)
    return school_name, maximum_class_size, total_students, teachers


def calculate(school_name, maximum_class_size, total_students, teachers):
    required_teachers = total_students // maximum_class_size
    if teachers > required_teachers:
        eg.buttonbox(f"There are {teachers - required_teachers} too many teachers at {school_name}.\n"
                     f"{school_name} has {teachers} teachers and only needs {required_teachers}", "Over-staffed", ["Ok"])
    elif teachers < required_teachers:
        eg.buttonbox(f"There are {required_teachers - teachers} too few teachers at {school_name}.\n"
                     f"{school_name} has {teachers} teachers and needs {required_teachers}", "Under-staffed", ["Ok"])
    else:
        eg.buttonbox(f"There are the correct amount of teachers at {school_name}.\n"
                     f"{school_name} has {teachers} teachers", "Correct staffing", ["Ok"])


def main():
    start = eg.buttonbox("Do you want to perform a calculation?", "Teacher Student Ratio", ["Yes", "No"])
    while start == "Yes":
        info = get_info()
        calculate(*info)
        proceed = eg.buttonbox("Do you want to perform another calculation?", "Teacher Student Ratio", ["Yes", "No"])
        if proceed == "No":
            break


main()
