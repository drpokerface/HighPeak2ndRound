import csv
dict = {}
with open('/content/sample_input.txt', 'r') as fd:
    reader = csv.reader(fd)
    i=0
    for row in reader:
      if(len(row)>0):
        i+=1
        if(i==1):
          num=int(row[0].split(':')[1])
        if(i>2):
          dict[row[0].split(':')[0]] = int(row[0].split(':')[1])  
        print(row[0].split(':'))

# Creates a sorted dictionary (sorted by key) 
dict = {'Fitbit Plus':7980,'IPods':22349,'Apple Band':999,'Cult Pass':2799,'Macbook Pro':229900} 


sorted_values = sorted(dict.values()) # Sort the values
sorted_dict = {}

for i in sorted_values:
    for k in dict.keys():
        if dict[k] == i:
            sorted_dict[k] = dict[k]
            break

print(sorted_dict)

#num=3
numEmployees=num-1
difference=[]

for i in range(len(list(sorted_dict.keys()))-numEmployees):
  diff=sorted_dict[(list(sorted_dict.keys())[i+numEmployees])]-sorted_dict[(list(sorted_dict.keys())[i])]
  difference.append(diff)
  low=min(difference)
startIndex=difference.index(min(difference))  

for k in range(startIndex,startIndex+num):
  print(list(sorted_dict.keys())[k],sorted_dict[list(sorted_dict.keys())[k]])  

file1 = open('sample_output.txt', 'w') 
s="The goodies selected for distribution are: \n"
file1.write(s) 



for k in range(startIndex,startIndex+num):
  s=(list(sorted_dict.keys())[k],sorted_dict[list(sorted_dict.keys())[k]])
  file1.write(str(s)) 

s="\n"
file1.write(str(s)) 

s="And the difference between the chosen goodie with highest price and the lowest price is "+str(low)
file1.write(str(s)) 


file1.close()