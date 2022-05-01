#****************recursive fanction**********
def function1(n):
    if n==1:
        return 1
    else:
       return (n*function1(n-1))

print(function1(5))

#****************fabonaci series by recursive function*****
#*** 0 1 1 2 3 5 8 13 21**********
def fucntion2(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fucntion2(n-1) + fucntion2(n-2)
    
print(fucntion2(8))