# ***** TUPLE ****

marks = (12 , 45, 76, 565, 12,12)
 
# marks[0] = 99  if we use this it will throw an error as tuple is immutable
print(marks.count(12))
print(marks.index(12))   # prit thhe index of the 12 which come first


#    ------*****  NOTE *****----
#   Look  () bracket is not necessary for defining tuple 
person = "ram", "Shyam", "abhi"
#  printing the person will give the tuple . so if we write anyhing without bracket then it is a tuple
print(person)


#    *** Set ****

#  if we want to store only the unique elments
marks = {12 , 45, 76, 565, 12,12}
print(marks)   # print 12 on;y 1 time not repetitive but the order is random  as there is no index in set 
#  so for traversing we have to run loop not use index 
for mark in marks:
    print(mark)   # not jave to give index

