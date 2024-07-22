f= open('new.txt')
check = f.read()
print(check)

f= open('new.txt', 'w')
f.write("Aman you have done it!")
f.close

f = open('new.txt', 'r')
f1 = f.read()
print(f1)

f = open('new.txt', 'a')
f.write(" now the data is appended .. ")
f.close

f= open('new.txt')
check = f.read()
print(check)
