import math
N=int(input())
a=[]
i=2
l=math.sqrt(N)
while i<l:
    if N%i==0:
        a.append(N)
        break
    i=i+1
if a!=[]:
    print('yes')
else:
    print('no')
