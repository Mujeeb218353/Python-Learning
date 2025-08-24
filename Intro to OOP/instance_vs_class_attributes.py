class Employee:
    language = "Python"
    salary = 1200000 

employee1 = Employee()

employee1.name = "Mujeeb Ur Rahman"
employee1.age = 22
employee1.contact = "03455109786"
employee1.language = "JavaScript" # Instance attribute is overriding the class attribute

print(employee1.name, employee1.age, employee1.contact, employee1.language, employee1.salary)