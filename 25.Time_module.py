#*************** time module in python ***************
import datetime
from tkinter import Y
#***************** get time now************
obj=datetime.datetime.now()#**********return current date and time
print(obj)
print(datetime.datetime(2022,3,14))

m=obj.strftime("%Y")
print(m)