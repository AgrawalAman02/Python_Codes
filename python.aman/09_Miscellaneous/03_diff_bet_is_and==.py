
# is compares the ecxact the location of two entity and == compares the values of both
a=4
b='4'

print(a is b) #exact location of obj in memory
print(a==b)  #value

p = [1,2,3,4]
q = [1,2,3,4]

print(p is q) # false
print(p ==q)  #true

r = 3
s = 3 

print(r is s) # true
print(r==s)  #true

# not like as list it gives true in both case 
# since constant is immutable(string,tuple) , so when immutable obj comes , then that created in memory only once and the all identifiers points that
# so address and value is both same

