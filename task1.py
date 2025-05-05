student_result = {'alice':85, 'Rocky':90, 'Bob':70,'dawood':60}
student_name = input("Enter the student's name: ")

if student_name in student_result:
    print("{}'s marks: {} " .format(student_name,student_result[student_name]))
else:
    print("student not found")