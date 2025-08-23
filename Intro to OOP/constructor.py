class Employee:
    language = "Python"
    salary = 1200000 


    def __init__(self, name, age, contact, language = "Python", salary = 1200000): # init is a dunder method which is automatically called
        self.name = name
        self.age = age
        self.contact = contact
        self.language = language
        self.salary = salary
        print("I am creating an object")

employee1 = Employee("Mujeeb Ur Rahman", 22, "03455109786")  

print(employee1.name, employee1.age, employee1.contact, employee1.language, employee1.salary)