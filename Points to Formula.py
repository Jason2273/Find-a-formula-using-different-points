import numpy
from decimal import *
from numpy.linalg import inv
getcontext().prec = 100

store = []
i=0
x=0
y=0
data1 = 0
data2 = 0

while str(data1) != "@" and str(data2) != "@":
  data1 = input("x")
  if data1 == "@":
    data2 = "@"
    i=i+1
    if data1 != "@" and data2 != "@":
      store.insert(i,[int(data1),int(data2)])
    else:
      store.insert(i,[0,0])
  else:
    data2 = input("y")
    i=i+1
    if data1 != "@" and data2 != "@":
      store.insert(i,[float(data1),float(data2)])
    else:
      store.insert(i,[0,0])
		    
del(store[i-1])
i=i-1

unknown = []
Calculate = []
temp = []
Result=[]

for x in range (0,i):
  temp.insert(x,0)

for z in range (0,i):
  unknown.insert(z,0)
  Calculate.insert(z,temp)

first = -1
second = 0

for x in range (0,i):
    first = first + 1
    second = 0
    for y in range (0, i):
      temp1 = store[first][0]
      temp2 = i-second
      getcontext().prec = 100
      temp3 = temp1 ** temp2
      Result.insert(y+5*x,temp3)
      second = second + 1

def split(arr, size):
     arrs = []
     while len(arr) > size:
         pice = arr[:size]
         arrs.append(pice)
         arr   = arr[size:]
     arrs.append(arr)
     return arrs

Calculate = split(Result, i)
abc=i

A=numpy.matrix(Calculate)
Ainv = inv(A)
B=[]
for y in range (1,abc+1):
  B.insert(y-1,store[y-1][1])

B = numpy.reshape(numpy.split(numpy.array(B),1),(abc,1))
Result = Ainv * B
numpy.set_printoptions(precision=120)
print(Result)

query1 = 0
Semi = numpy.split(Result,abc)
while query1 != "@":
  query1 = input('x')
  input2 = round(float(query1),2)
  outputy = 0
  
  for i in range (0, abc):
    outputy = outputy + Semi[i]*(input2**(abc-i))
  print(round(float(outputy[0]),3))