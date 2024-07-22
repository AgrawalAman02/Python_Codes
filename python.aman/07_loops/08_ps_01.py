#  multiplication table
n= int(input("enter the no. whose table u want : "))

table =1
for i in range(1,11):
    table= n*i
    # print(table)    # or below
    print(str(n)+" X "+str(i) + "="+ str(i*n))

    # or using fstring
    print(f"{n} X {i} = {n*i}")