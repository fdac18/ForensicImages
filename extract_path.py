import os
import csv


dirs =  ['2011', '2012', '2013', '2014', '2015', '2016']
all_dir = []
for di in dirs:
    all_dir.extend([x[0] for x in os.walk(di)])
res = []
size = len(all_dir)
for i in range(size-1):
    if all_dir[i] not in all_dir[i+1]:
        res.append(all_dir[i])
 
with open ("paths.csv", 'w') as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(res)

