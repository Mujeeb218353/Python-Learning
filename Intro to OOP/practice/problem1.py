class Programmer:
    def __init__(self, name, age, contact, language, salary):
        self.name = name
        self.age = age
        self.contact = contact
        self.language = language
        self.salary = salary

programmer = Programmer("Mujeeb Ur Rahman", 22, "03455109786", "Python", 1200000)

print(programmer.name, programmer.age, programmer.contact, programmer.language, programmer.salary)