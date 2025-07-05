def calculate_grade(marks):
    if marks >= 90:
        return 'A+'
    elif marks >= 80:
        return 'A'
    elif marks >= 70:
        return 'B'
    elif marks >= 60:
        return 'C'
    else:
        return 'Fail'

def main():
    num_students = int(input("Enter number of students: "))
    
    for i in range(1, num_students + 1):
        print(f"\nEnter details for student {i}:")
        name = input("Enter name of student: ")
        marks = float(input("Enter marks out of 100: "))
        
        grade = calculate_grade(marks)
        print(f"{name} scored {marks} and got grade: {grade}")

main()
