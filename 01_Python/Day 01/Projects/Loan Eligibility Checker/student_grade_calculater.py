# Student Grade Calculator
# The program will ask for:
# Student Name
# English Marks
# Maths Marks
# Science Marks
# Social Marks
# Computer Marks

# Then it will calculate:

# Total Marks
# Percentage
# Grade

student_name = input("Enter your Name: ")
english_marks = int(input("Enter your English Marks: "))
maths_marks = int(input("Enter your Maths Marks: "))
science_marks = int(input("Enter your Science Marks: "))
socail_marks = int(input("Enter your Social Marks: "))
computer_marks = int(input("Enter your Computer Marks: "))

total_marks = english_marks + maths_marks + science_marks + socail_marks + computer_marks
percentage = (total_marks/500) * 100

print("=" *50)
print("---STUDENT GRADES---")
print("=" *50)

print(f"Student Name: {student_name}")
print(f"Percentage : {percentage}")
print(f"Total Marks : {total_marks}")

if percentage >= 90:
    print("Grade : A")
elif percentage >= 80:
    print("Grade : B")
elif percentage >=50:
    print("Grade : C")
else:
    print("Grade : D")

