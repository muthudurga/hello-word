import math
N,M=input().split()
x=int(N)*int(M)
a=math.sqrt(x)
b=int(math.sqrt(x))
if a==b:
    print('yes')
else:
    print('no')
