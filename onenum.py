N=int(input())
x=[int(x) for x in input().split()]
z=[]
y=[]
if len(x)==N:
    for i in range(N):
        if x[i] in z:
            y.append(x[i])
        else:
            z.append(x[i])
    for i in range(len(z)):
        if z[i] not in y:
            print(z[i])
