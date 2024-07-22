## question 1

# myDict = {
#     "pankha" : "Fan",
#     "dabba" : " box",
#     "vastu": "item"
# }
# print("options are ", myDict.keys())
# a=input("enter the hindi word\n")
# # print("the english word is ", myDict[a])

# # below line will not deliver any error if we enter any hindi word which is not the key in dictionary
# print("the english word is : ", myDict.get(a))

## question 2
# num1 = int(input("enter no. 1 : "))
# num2 = int(input("enter no. 2 : "))
# num3 = int(input("enter no. 3 : "))
# num4 = int(input("enter no. 4 : "))
# num5 = int(input("enter no. 5 : "))
# num6 = int(input("enter no. 6 : "))
# num7 = int(input("enter no. 7 : "))
# num8 = int(input("enter no. 8 : "))

# set = {num1,num2,num3,num4,num5,num6,num7,num8}
# print(set)

## question 3
# # can we have a set with 18 as int and 18 as str as its values
# set = {18, "18"}
# print(set)
# # yep we got both value means both are not identical

## question 4

# s= set()
# s.add(20)
# s.add(20.0)
# s.add("20")
# #  we think the length of s is 3 
# print(len(s))  # but it gives 2
# #  as pyhton count same int and float value as identical 
# print(s)

## Question 6

favlang = {}
a= input("enter your favourite language aman : ")
b= input("enter your favourite language shubham : ")
c= input("enter your favourite language sonali : ")
d= input("enter your favourite language harshit :  ")
favlang['aman'] = a
favlang['shubham'] = b
favlang['sonali'] = c
favlang['harshit'] = d
print(favlang)

 