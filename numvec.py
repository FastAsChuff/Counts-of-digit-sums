#https://math.stackexchange.com/questions/5061783/how-many-vectors-have-a-given-sum-of-digits
#Author: Simon Goater
#Free to use, copy, and modify with conspicuous attribution, for non-commercial use only.
import math

def numvec(m,k): #Number of sequences of the digits 0-9 of length m with sum k
  if m <= 0:
    return 0
  if k > 9*m:
    return 0
  if k < 0:
    return 0
  if (k < 10) and (m == 1):
    return 1
  sum = 0
  for digit in range(10):
    sum += numvec(m-1,k-digit)
  return sum
  
def numvecdictsinit(m,k,numvecdicts): #Dynamic programming approach
  numvecdicts.append({0:1,1:1,2:1,3:1,4:1,5:1,6:1,7:1,8:1,9:1})
  k = min(k, 9*m-k)
  for j in range(10,k+1):
    numvecdicts[0][j] = 0
  for i in range(1,m):
    numvecdicts.append({})
    for j in range(k+1):
      sum = 0
      for s in range(10):
        if j - s >= 0:
          sum += numvecdicts[i-1][j-s]
      numvecdicts[i][j] = sum
    numvecdicts[i-1] = 0 #Uncomment for better RAM efficiency if only final row is required.
    
m = 100
k = 230
numvecdicts = []
#Print number of 0-9 digit sequences of length m with element sum k
#print(numvec(m,k)) # Slow!
numvecdictsinit(m,k,numvecdicts)
print(numvecdicts[m-1][min(k, 9*m-k)]) # Fast!
print(f"{1+math.floor(math.log10(numvecdicts[m-1][min(k, 9*m-k)]))} digits.") 
#for i in range(m):
#  row = []
#  for j in range(k+1):
#    ix = min(j, 9*(i+1)-j)
#    if ix >= 0:
#      row.append((j,numvecdicts[i][ix]))
#  print(f"{i+1} : {row}")
