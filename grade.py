'''i went a little further than the requirement :)'''

grades ={"Abenezer":"A",
       "Biniyam":"A-",
       "Amen":"A",
       "Eyasu":"B",
       "Israel":"C"}
def get_grade(grades,student_name):
    try :
        student_name=student_name.title()
        if student_name in grades.keys():
            return(grades.get(student_name))
        else:
            raise KeyError
    except KeyError:
        return "student doesn't exist please try again!"


def login():
        while True:
            print("student portal")
            print("\n"+"="*20)
            login_as=input("HI there, how would you want to log in(Admin or User).\ninput return to exit portal.\n")

            if login_as.lower() =="admin":
                while True:
                    action=input("Enter the action you want to perform (remove grade, review grade, add grade, update grade)\ntype return to exit\n")
                    if action.lower()=="remove grade":
                        removed_student=input("Enter the name of the student to be removed\n")
                        removed_student=removed_student.title()
                        if removed_student in grades.keys():
                            grades.pop(removed_student)
                            print(f"✓ Successfully removed {removed_student}")  # CONFIRMATION
                        else:
                            print("student not found!")
                        print("type return to exit")
                    elif action.lower()=="add grade":
                        added_student=input("enter the name of the student.\n")
                        added_grade =input("enter added grade.\n")
                        added_grade=added_grade.upper()
                        added_student=added_student.title()
                        grades.update({added_student:added_grade})
                        print(f"✓ Successfully added {added_student} with grade {added_grade}")  # CONFIRMATION
                    elif action.lower()=="update grade":
                        updated_student= input("Enter the name of the student.\n")
                        updated_grade= input('Enter the grade\n')
                        updated_grade=updated_grade.upper()
                        updated_student=updated_student.title()
                        grades.update({updated_student :updated_grade})
                        print(f"✓ Successfully updated {updated_student} to grade {updated_grade}")  # CONFIRMATION
                    elif action.lower()=="review grade":
                        display= input("Enter the name of the student.\n")
                        display=display.title()
                        if display in grades.keys():
                            print(grades.get(display))
                    elif action.lower()=="return":
                        break
                    else:
                        print("invalid action please try again!")    

            elif login_as.lower() =="user":
                name= input("please enter your name\n")
                result=get_grade(grades,name)
                print(result)
            elif login_as.lower() =="return":
                print("Thank you for using our portal")
                break
            else:
                print("invalid input!")


def main():
    print("\n"+"="*20)
    print("STUDENT GRADE PORTAL")
    print("\n"+"="*20)
    login()


main()