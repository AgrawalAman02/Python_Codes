a = input("enter the number(Enter some string to see the errors): ")
print(f"Multiplication table of {a} is : ")


# for i in range(1,11):
#         print(f"{int(a)} X {i} = {int(a)*i}")
# if i enter a = aman i.e. a string but a is int so the error occoured
# and the program ends there means after that  the print statement or any other not work
# but if we use  anything in try then if that statement gives an error then except works 
try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print(e)
#  here e means errors .so print e means it will print the errors
# otherwise we can write any otherthing in print i.e. print(invalid) so it will print invalid in place of error
# except:  if we arenot using e
# print("Invalid entry!")
print("some line of codes")
print("end of the program\n\n\n")


# we ca also handle some specific error
try:
    num = int(input("Enter an index : "))
    a= [6,3]
    print(a[num])
except ValueError:  # tis will handle the invalid value error
    print("Number entered is not a integer...")
except IndexError:  # this will handle the invalid index error only
    print("Index error")