import statistics
import math
num_array = list()
num = input("Enter how many elements you want:")
print ('Enter numbers in array: ')
for i in range(int(num)):
    n = input("num :")
    num_array.append(int(n))
avg=statistics.mean(num_array)
i=0
var=0
for i in range (0,len(num_array)):
    var=var+((num_array[i]-avg)**2)
std=math.sqrt(var)
print("voryans= " + str(var) )
print("std=" +str(std) )

