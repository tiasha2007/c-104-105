import csv
import math

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

#Sorting the data to get the list
data=file_data[0]

def mean(data):
    n=len(data)
    total=0
    for x in data:
        total+= int(x)
    
    mean=total/n
    return mean

# Squaring and getting the values
squared_list=[]
for number in data:
    a=int(number)-mean(data)
    a=a**2
    squared_list.append(a)

# Getting the sum
sum=0
for i in squared_list:
    sum=sum+i

# Dividing the sum by total value
result=sum/(len(data)-1)

# Getting the deviation by taking sqaure root of the result
std_deviation=math.sqrt(result)

print(std_deviation)
