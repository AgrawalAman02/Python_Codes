try:
    l = [1,2,5,7]
    i = int(input("Enter an index : "))
    print(l[i])
except :
    print("Some error occured")

finally:
    print("Whether try works or except , I am alaways executed")


'''
SO question arises that why do we need finally, if we can simply wrint print in the last  and that print simply works
so in case of function is try ,except and finally is given and break is there in all then if try/except works then it retured but not print simple print after that
but it will print the finally statement whehter return occiur or not
'''