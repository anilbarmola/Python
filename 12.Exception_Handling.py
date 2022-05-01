#Try Except Exception handling in python
# baad ka code chalta rhe programme error throw na kre is liye hma try except exception ka use krte h

from logging import exception


print("enter the num")
x=input()
print("enter the second num")
y=input()#if i give sting vaule it will show error
try:
    print("the sum is :", x+y)
except exception as e:
    print(e)

print("further progrmmer will be run ")