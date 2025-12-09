def get_student_score():
    scores = {'John': 85, 'Sara': 92, 'Mike': 78}
    
    name = input("Enter student name: ").strip()
    name=name.title()
    
    try:
        score = scores[name]
        print(f"{name}'s score: {score}")
    except KeyError:
        print("Student not found!")

def main():
    get_student_score()


main()