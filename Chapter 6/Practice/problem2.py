a = int(input("Enter subject 1 marks:"))
b = int(input("Enter subject 2 marks:"))
c = int(input("Enter subject 3 marks:"))
total = a+b+c
total_percentage = (total/300)*100

if total_percentage >= 40 and a >= 33 and b >= 33 and c >= 33:
    print("Pass")
else:
    print("Fail")