myDict = {
    "fast": "In a Quick Manner",
    "harry": "A Coder",
    "marks": [1,2,5],
    "anotherDict": {
        'harry': 'Player'
    },
    1:2  # it is also a key
}
print(myDict.keys())
print(type(myDict.keys()))
# so type will be dict keys(another type) not list 
# but we can change into list by:
print(list(myDict.keys()))  # we can print in any ways i.e in list way or dict keys way

# to print the values of keys :
print(myDict.values())
# if we want to print in list then we can print it 

# to prints the (key, value )for all contents of the dictionary
print(myDict.items())

# to update the dictionary
print(myDict)
updateItemsDict = {
    "lovish": "friend",
    "divya": "gf",
    "shubham": "bokka"
}
myDict.update(updateItemsDict)  # Updates the dictionary by adding key_value pairs from updateDict
print(myDict)

print(myDict.get("harry"))  # returns its value but we also do it by print(mydict["harry"]) so what is diff

# the diff betn .get amd [] syntax method
print(myDict.get("harry2")) # returns None as harry2 is not present in the dictionary
# print(myDict["harry2"])    # throws an error as harry 2 is not present