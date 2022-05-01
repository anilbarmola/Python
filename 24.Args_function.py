#*******************   *args  *********
#  *args is use for send multipla value in argument

def function1(*args, **kwargs):
    print(*args)
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key} is a {value}")
    

var=["anil","Python","c++","excel","R","Data Science"]# we can add multipal items  here


#******************         **kwargs         **************
kw={"anil":"data analysis","mohit":"chief","rohit":"dance"}
function1(*var , **kw)