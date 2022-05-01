#claculor using if condions
print("Enter your first num")
x=int(input())
print("Enter your second num")
y=int(input())
print("press 1 for add, 2 for subtact, 3 for multiply and 4 for division")
z=str(input())
if  z==1:
  print("sum is ", x+y)
elif z==2:
  print("Subtraction is: ",x-y)
elif z==3:
  print("Multiplication is: ",x*y)
elif z==4:
  print("Division is: ",x/y)
else:
  print("! Wrong input!!!")

