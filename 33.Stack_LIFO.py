#************ stack in python*******
#************* stack is liner data structure********
#********** Stack work in LIFO***** last in first out********
#******PUSH(Insert element), POP(del), PEEK(show last element), DISPLAY************

from pickle import TRUE


l=[]
while TRUE:
 c=int(input('''
    1 to append list
    2 for Pop element
    3 show peek element
    4 display list
    5 for exit'''))
 if c==1:
    n=int(input("Enter the element"))
    l.append(n)
    print(l)
 elif c==2:
     if len(l)==0:
         print("Empty stack")
     else:
         p=l.pop()
         print(p)
         print(l)
 elif c==3: 
    print("the last element is", l[-1])
 elif c==4:
     print(l)
 elif c==5:
     break