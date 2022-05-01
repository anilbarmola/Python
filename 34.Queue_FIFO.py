#***************** queue in python***********
#********** FIFO******First in first out*******
#********Enqueue(add element), dequeue(remove element), front(get first element), rare(last element)
l=[]
while True:
 c=int(input('''
    1 EnQueue
    2 DeQueue
    3 Front Element of Queue
    4 Last Element of Queue
    5 Show Queue
    6 for exit'''))
 if c==1:
    n=int(input("Enter the element"))
    l.append(n)
    print(l)

 elif c==2:
     if len(l)==0:
         print("Empty Queue")
     else:
         del l[0]
         print(l)
 elif c==3: 
    print("The First element is", l[0])
 elif c==4: 
    print("The last element is", l[-1])
 elif c==5:
     print(l)
 elif c==6:
     break