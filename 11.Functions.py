#************Function in python************
#**********user define function***
def function1(a,b):
    sum=a+b
    print(sum)
function1(4,7)
#*************************************
def function2(c,d):
    """this fuction do average of two numbers"""#doc sting for fuction. its help
    ave=(c+d)/2
    return ave
var=function2(6,12)
print(function2.__doc__)# calling doc string for fucntion2
print(var)

#***********************************