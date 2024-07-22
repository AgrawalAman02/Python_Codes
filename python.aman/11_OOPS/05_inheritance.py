class Employee:
    def __init__(self, name,id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of employee : {self.name} is {self.id}")

# if we want to rename the class Emoloyee with somme added property . but when we do it it will throw errors
# so we use inheritance

class Programmer(Employee):
    def showLanguage(self):
        print("the default language is Pyhton")

e = Employee("Rohan Das", "2210901201")
e.showDetails()
# e.showLanguage will not work  . we first havr to create an instance of programmer class
e1 = Programmer("aman", "212123")
e1.showLanguage()
e1.showDetails()
# so we can use the details of employe as we inherit it
