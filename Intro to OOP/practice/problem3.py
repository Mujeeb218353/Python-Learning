class Employee:
    salary = 1200000
    language = "Python"    # Class attribute does not change


employee1 = Employee()

employee1.salary = 1500000
employee1.language = "JavaScript"  # Instance attribute will change

print(employee1.salary, employee1.language, Employee.salary, Employee.language)