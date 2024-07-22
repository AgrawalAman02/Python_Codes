# def double(x):   # function to find the square of x
#     return x*2

# we can use lambda function to find it too
double = lambda x: x*2
cube = lambda x: x*x*x
# it is a easy way to write short function into one liner not for long f(x)
avg = lambda x,y,z: (x+y+z)/3  # so it can take multiple value as input

#most imp is that this lambda is used when we passed functuon as arguement of another function .
#then we need a one liner function so there we used this lambda
# lets below first we see hoe a functionis paased
def apply(fx,value):
    return 6+ fx(value)    # here we r returning the  sum of 6 and result of fx 

print(double(5))
print (cube(5))
print(avg(3,5,10))
print(apply(cube,6))  # here we are passing cube function as an arguement to fx in apply
#so we can without making a def cube funtion, directly pass lambda f(x)
print(apply(lambda x: x*x*x,6))

# solambda is a anonymous f(x) as we are passing lambda as cube fx without letting know that it is cube fx
