# I renamed the name of csv file to project.csv
import csv
from collections import Counter

with open("project.csv",newline = '') as f:
    reader = csv.reader(f)
    data = list(reader)
data.pop(0)
new_data = []
for i in range(len(data)):
    num = data[i][1]
    new_data.append(float(num))


                                            #Mean

n = len(new_data)
sum = 0
for i in new_data:
    sum = sum+i
mean = sum/n
print("Mean =" + str(mean))   

                                            #Mode

data1 = Counter(new_data)
mode_data_for_range = {
    '50 - 60':0,
    '60 - 70':0,
    '70 - 80':0,
}
for height,occurence in data1.items():
    if 50 < float(height)<60:
        mode_data_for_range['50 - 60'] += occurence
    elif 60 < float(height)<70:
        mode_data_for_range['60 - 70'] += occurence
    elif 70 < float(height)<80:
        mode_data_for_range['70 - 80'] += occurence
  
mode_range,mode_occurence = 0,0
for range,occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range,mode_occurence = [int(range.split('-')[0]),int(range.split('-')[1])],occurence
mode = float((mode_range[0]+mode_range[1])/2)
print("Mode =" + str(mode))   

                                            #Median

n = len(new_data)
new_data.sort()
if n%2 == 0 :
    median1 = float(new_data[n//2])
    median2 = float(new_data[n//2-1])
    median = (median1 + median2)/2
else:
    median = new_data[n//2]

print("Median =" + str(median))   