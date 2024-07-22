# sets are unordered
# sets are unindexed
# there is no way to chnge items on set
# sets cant contain duplicate values
b=set()
print(type(b))
#  if we want to add any item to this empty set then we use add method
b.add(4)
print(b)
b.add(5)
b.add(5)
print(b)

# can we add a list to the set 
# b.add([1,2,3])
# no it gives error as list are unhashable i.e cant be add
# we cant also add dictionary as it is also unhashable
# but we can  add tuple 
b.add((1,2,4,3))
print(b)

print(len(b))  #print the length of set


b.remove(4)  # to reomove any element
print(b)     # see we removed it

# b.remove(15)  gives error as 15 not present

## pop remove the random element from thr set and returns the element removed
b.pop()
print(b)


## b.clear()  :: empties the set b

## b.union :: returns a new set with all items from both sets => {}
##b.intersection({}) :: returns a set which contains only items availablr on both sets
