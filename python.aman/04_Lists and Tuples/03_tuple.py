# creating a tuple by using ()
t=(1,2,4,5)
# printing  a tuple
print(t[0])

# cannot update the values of a tuple  (diff from list)
# t[0]= 34  # it gives TypeError: 'tuple' object does not support item assignment
a=() #empty tuple
print(a)
t1=(1)   # wrong way to declare a tuple with single element as it shows it as a no.
t1=(1,)  #tuple with single element must requires a comma
print(t1)
