a = int(input("Enter a value between 5 amd 9 : "))

if(a>5 or a>9):
    raise ValueError("Value should be between 5 and 9")     