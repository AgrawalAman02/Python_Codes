a= input("enter your name : ")
print(a)
b= input("enter your age: ")
print(b)
print(type(b))
#so the age returned will be of str type as per last print statement.
#  thus we have to typecast it to use as int or other  we cant add anything to b
b= int(b)  #convert to int if posible
print(type(b))
print(b+8)
