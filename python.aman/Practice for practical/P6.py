marks = [97  , " aman" , 78, 90]
marks.append(786)
marks.insert(2,87)
print(marks)
 
# to that that element is present in the list or not we use in keyword
print(99 in marks)

i = 0
while i< len(marks):
    print(marks[i])
    i = i +1


#  for clearing the list we use clear function
marks.clear()
print(marks)  # it will print the empty list