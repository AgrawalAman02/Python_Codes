class Person:

    #constructor definition:
    def __init__(self,name,occupation):   #this helps in making constructor
        print("Hey I am a person")
        self.name = name
        self.occupation = occupation


# constructor taking arguement is called parameterised constructor
# And that only taking self is Default constructor
    name = "harry"
    occupation = "Software Engineer"
    networth = 10
    def info(self):   # self is just like this in java . i.e. it is refering to instance of this class
        print(f"{self.name} is a {self.occupation}")
    # self is necessary to provide in a method in class in most of the case

a = Person("Divya","HR")  # so everytime we create a function , the consructor will be called
# a.name = "Divya"
# a.occupation = "HR"   # for oassing these things in at the time of creating an object then we use constructer
a.info()
# so see the benefit of constructor
b = Person("Aman", "Student")
b.info()
