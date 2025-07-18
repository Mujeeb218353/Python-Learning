sub1 = int(input("Enter subject 1 marks: "))
sub2 = int(input("Enter subject 2 marks: "))
sub3 = int(input("Enter subject 3 marks: "))

total_obtained_marks = sub1 + sub2 + sub3
total_marks = 100 * 3
percentage = (total_obtained_marks / total_marks) * 100

if percentage >= 90 and percentage <= 100:
    grade = 'A+1'
elif percentage >= 80 and percentage < 90:
    grade = 'A'
elif percentage >= 70 and percentage < 80:
    grade = 'B'
elif percentage >= 60 and percentage < 70:
    grade = 'C'
elif percentage >= 50 and percentage < 60:
    grade = 'D'
elif percentage >= 40 and percentage < 50:
    grade = 'E'
else:
    grade = 'F'
    
print("Grade:", grade)