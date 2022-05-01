#**********Global and Local Variable****
from re import L


l=10# l is global variable
m=8# m is also globla variable
def function1():
    l=18# this is local variable
    n=9
    print(m)#calling global variable inside the fucntion
    print(l)# this will pirnt local variable
    return 0
function1()
print(l)#this will print global variable

#************invoke global variable inside the function*****
#********by using global key word*************
def functin2():
    global l
    l=23+l #updating golbal variable inside the fucntion using global key word
    print(l)
    return 0
functin2()