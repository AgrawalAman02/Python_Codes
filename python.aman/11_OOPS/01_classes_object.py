class Person:
    name = "harry"
    occupation = "Software Engineer"
    networth = 10
    def info(self):   # self is just like this in java . i.e. it is refering to instance of this class
        print(f"{self.name} is a {self.occupation}")

a = Person()
print(a.name)
a.name = "Shubham"
a.occupation = "Accountant"
print(a.name,a.occupation)
a.info()

b = Person()
b.name = "Aman"
b.occupation = "CA"
b.info()

c = Person()
c.info()
# as we havent fiven any thing to c so the default values will be printed