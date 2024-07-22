from functools import reduce

# ------------------------------------------------------MAP---------------------------------------------------------
def cube(x):
    return x*x*x

print(cube(3))
# tjis is for finding cube
# now if i a list we want a new list where each element is the cube of earlier list's element
# so what we di is below
l = [ 1,2,3,4,5,6,7]
# newl = []
# for item in l:
#     newl.append(cube(item))
# print(newl)
# we can do it b shrtcut i.e.map

newl = map(cube,l)
print(newl)
# but it will return as an map object. so  we need to typecast it in list
# newl = list(map(cube,l))
# so we give a function(may bea lambda function also) as an arguement in map and the the item where map of that function to done
# so here we are applying map function to each element of lst l
newl = list(map(lambda x: x*x*x,l))
# so it give same outputwhen used as lambda function
print(newl)

# --------------------------------------------FILTER-----------------------------------------------
# it is used to filter the thin for eg list to get something and remove something on the basis of function
def filter_function(a):
    return a>4
newnewL = filter(filter_function, l)
print(newnewL)
# it will also giee filter object .so it should be converted to list
print(list(newnewL))

# so a function takes anorhwer funvtion as am arguement thrn it is called as higher order functiom
# we can aso take lambda aa a function in filter
#  so the function in filter known as predicate is a boolen type fx which whn returns true then filter work oterwise filtered .

# -------------------------------------------------------REDUCE-------------------------------------------------
# it needs to be import
numbers = [1,2,3,4,5,6]
# calculate the sum of the nu.s using the rduce function
sum = reduce(lambda x,y: x+y,numbers)
# it sum first two, then third one with the output of first two then so on...
print(sum)