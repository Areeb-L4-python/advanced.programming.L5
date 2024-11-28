from random import randint
from operator import itemgetter

def add_student(student_list, student_number, module_code, grades):
    student_list.append([student_number, module_code, grades])
    return student_list

def generate_student_number(student_name):
    num = randint(100, 999)

    names = list(student_name.split(" "))

    initials = names[0][0].lower() + names[1][0].lower()

    student_number = initials + str(num)
    return student_number

def validate_student_number(student_list, student_number):
    for student in student_list:
        if student_number == student[0]:
            return True
        else:
            return False

def enter_grade():
    grade_1 = int(input("Please enter your first grade: "))
    grade_2 = int(input("Please enter your second grade: "))
    # Give default grade as zero
    grades = [grade_1, grade_2]
    return grades

def change_grade(student_list, student_number):
    i = int(input("Which grade would you like to replace? 1 or 2 "))
    new_grade = int(input("Please input your new grade: "))
    for student in student_list:
        if student_number == student[0]:
            grades = student[2]
            if i == 1:
                grades[0] = new_grade
            elif i == 2:
                grades[1] = new_grade
            else:
                break
            print(grades)
        else:
            break

    return

def remove_student(student_list):
    student_num = int(input("Please enter the student_number of the student you wish to remove: "))
    for student in student_list:
        if student_num == student[0]:
            is_sure = input(f"Are you sure you really want to delete {student_num} from the database? ")
            if is_sure:
                student_list.remove(student)
                print(f"Student successfully deleted")
            else:
                break
        else:
            break

    return student_list

def generate_report(student_list):
    for index, student in enumerate(student_list, start=1):
        print(f"Student {index} - Student ID: {student[0]} - Module Code: {student[1]} - Grades: {student[2]}")
    return

def generate_ranked_report(student_list):
    for index, student in enumerate(student_list, start=1):
        grades = student[2]
        average = sum(grades) / 2
        grades.insert(0, average)
        ranked_list = sorted(student_list, key=itemgetter(2))
    
    for index, student in enumerate(ranked_list, start=1):
        print(f"Rank {index}: {student[0]} with an average score of {student[2][0]}")

    return


def main():
    student_list = [[12345, 67, [99, 99]], [54321, 77, [45, 78]], [56789, 90, [61, 68]]]
    while True: 
        choice = int(input("Would you like to: 1. Add a student; 2. Remove a student; 3. Change a student's grades; 4. Generate a report; 5. Generate a ranked report; 6. Exit? "))
        match choice:
            case 1:
                module_code = randint(10,99)
                student_name = input("what is the student's name? ")
                student_number = generate_student_number(student_name)
                grades = enter_grade()
                add_student(student_list, student_number, module_code, grades)
                print(student_list)
            
            case 2:
                remove_student(student_list)

            case 3:
                student_number = int(input("Please enter in the number of the student whose grade you wish to change: "))
                print(validate_student_number(student_list, student_number))
                if validate_student_number(student_list, student_number):
                    change_grade(student_list, student_number)
                else:
                    print("You did not provide a valid student number")

            case 4:
                generate_report(student_list)

            case 5:
                generate_ranked_report(student_list)
            
            case 6:
                print("Program exited")
                exit()
            
            case _:
                print("Please enter a valid input: ")

if __name__ == "__main__":
    main()