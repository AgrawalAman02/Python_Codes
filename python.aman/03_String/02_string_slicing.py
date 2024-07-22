# greeting = "good morning, "
# name = "Harry"
# print(type(name))
# c = greeting + name
# print(c) # this will concatenate the string



# name= "Harry"
# print(name[0])
# # name[3] = "d"  (dont give hardy)-> doesnot work as 'str' object does not support item assignment

# print(name[0:3])   # give name of 0,1,2 not 3  # string slicing
# print(name[:4])    # vacant place auto become 0 i.e name[0:4]
# print(name[0:])   # print until last i.e. same as name[0:5] 0 to length
# c= name[-4:-1]  # is same as name[1:4]
# print(c)


# slicing with skip value
word = "amazing boy"
print(word[1:6:1])  # print from 1 to 6 with skip value 1 means no skip
print(word[0:6:2])  # print from 0 to 6 with every second character to be skipped
print(word[1::3]) #from 1 to last i.e. length with s value 2
