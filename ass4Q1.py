#Q1
#Example input
'''
100,0,0,0,100,100,100
1000,20.892,986,602,138.97,206.2,10.44
200,25,25,10,1,50,25,140,30
'''


import sys
import math


carLimit = 100 #limit of 100km
def distance(x1,y1,x2,y2): #x and y coordinates from the input
  x = (x1 - x2) * (x1 - x2) #matrix
  y = (y1 - y2) * (y1 - y2)
  return math.sqrt(x + y)


for line in sys.stdin:
  if 'Exit' == line.rstrip():
    break
  list = line.rstrip().split(",")

  newList = []
  for i in list:
    newList.append(float(i))
  
  size = len(newList)
  totalDistance = 0
  i = 1
  
  while (i < size):
    flag = 0
    for j in range(size-2,i,-2):
      newDistance = distance(newList[i],newList[i+1],newList[j],newList[j+1])
      
      if(newDistance <= carLimit):
        totalDistance = totalDistance + newDistance
        i = j
        flag = 1
        break
    
    if(flag == 0):
      break

  if(totalDistance == 0):
    print('-1')
  else:
    print('{:.2f}'.format(totalDistance))
