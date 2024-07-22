myDict = {
    "Fast": "In a Quick Manner",
    "Harry": "A Coder",
    "Marks": [1,2,3],
    1 : 76876,
    "anotherDict": {
        'harry': 'Player'
    }
}
myDict["Fast"] = "bokka"
print(myDict)
print(type(myDict[1]))

print(myDict['Fast'])
print(myDict['Harry'])
print(myDict['Marks'])
print(myDict['anotherDict'])

# there is no order in dictionary
# dictionary is mutable i.e we can change the value
# .i.e
myDict['Marks']= [1,4,5,7,8]
print(myDict['Marks'])