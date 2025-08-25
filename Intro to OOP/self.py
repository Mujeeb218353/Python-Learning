class Employee:
    language = "Python"
    salary = 1200000 

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Hello, have a nice day!")

employee1 = Employee()  

employee1.name = "Mujeeb Ur Rahman"
employee1.age = 22
employee1.contact = "03455109786"
employee1.language = "JavaScript"

print(employee1.name, employee1.age, employee1.contact, employee1.language, employee1.salary)
employee1.getInfo()
employee1.greet()