import os
import sys
import numpy as np

# Grab data file
src = os.chdir('C:\\Users\\wei\\imported_data.csv')

x_values = []
label = []

for row in src:
  datum = row.strip().split(',')
  x_values.append(datum)

data_set_row = len(x_values)
data_set_col = len(x_values[1])

tp = [0]*3
number_of_columns = []

for col in range(data_set_col):
  for row in x_values:
    try:
      a = float(row[col])
      if isinstance(a, float):
        tp[0] += 1
    except ValueError:
      if len(row[col]) > 0:
        tp[1] += 1
      else:
        tp[2] +=1
        
  number_of_columns.append(tp)
  tp = [0]*3

sys.stdout.write("Col#" + '\t' + "Number" + '\t' + "Strings" + '\t' + "Other\n")
iCol = 0
for types in number_of_columns:
  sys.stdout.write(str(iCol) + '\t\t' + str(types[0]) + '\t\t' + str(types[1]) + '\t\t' + str(types[2]) + "\n")
  iCol += 1
  

