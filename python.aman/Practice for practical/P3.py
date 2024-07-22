# String

name = "Aman Kumar"

print(name.upper())
print(name)
print(name.lower())

# to find a substring of a string we use find  : it return the index of the substring and return -1 if not got the substring
print(name.find("K"))
print(name.find("man"))  #return staring index

print(name.replace("Aman", "shekhar"))
print(name)  # still print Aman Kumar as string doesnot changes in original string

#  as find give -1 when thatthing is not present in the string 
#  but if we want to only check but not return index value then we use ** in ** keyword 

print("ironman" in name)
print("Aman" in name)