def greet(fx):
    def mfx():
        print("Good Morning!")   
        fx()
        print("Thanks for using this function")
    return mfx

@greet
def hello():
    print("Hello World")

def add(a,b):
    print(a+b)
# for using greet in add we needd to passed arguement . so we give *args , **kwargs as parameter in greet fx which represent tuple and dictionary resp.

hello()
# greet(hello)()    we  can also write in this way
# so we want to add greeting before and after the methods of fx 
# so in which fx we want decoration then we use @greet before that and we ahd define greet also 
