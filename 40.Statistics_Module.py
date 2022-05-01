#***************Statistics Module in Python****************
import statistics
l=[1,2,3,4,4,4,4,9,15,2,55,4,6,5,5,6,7,8,9,15,20,16,4,5,2,]
#*******Mean()**********sum of all div by total num********

print(statistics.mean(l))

#******** medain()*****it return the middle value of the data****
print(statistics.median(l))

#**********mode()******it return the most common data that occurs in list********
print(statistics.mode(l))

#*************Stdev()********it calculate the standard deviation to given data**
print(statistics.stdev(l))

#************median_low()**************it return low median of data**
print(statistics.median_low(l))

#****************median_heigh()***************it retun hight median data*****
print(statistics.median_high(l))

