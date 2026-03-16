
D = {}
num_students = 60
for i in range(1, num_students + 1):
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    grade = input("Enter Grade: ")
    attendance = input("Enter Attendance: ")
    D[i] = {"roll no": roll_no, "name": name, "grade": grade, "attendance": attendance}

for roll, details in D.items():
    print(f"Roll Number {roll}: {details}")
