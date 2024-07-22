marks = [1,34,78,97,43,56,90,1,32]

# idx = 0;
# for mark in marks:
#     print(mark)
#     if(idx==3):
#         print("Harry, awesome!")
#     idx+=1


# so we needto amintain the incremancy of extra operator hrer 
# so using enumerate we can avoid it
for idx,mark in enumerate(marks):
    print(mark)
    if(idx==3):
        print("Harry, awesome!")

print( )
fruits =['apple', 'banana', 'mango']
for idx , fr in enumerate(fruits):     #we can also give the start value from where idx start as arguement enumerate(fruits, start =1) , !0 if u want
    print(idx, fr)
