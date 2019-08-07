N=int(input())
x=str(N)
a=[]
for i in range(len(x)):
    if int(x[i])%2!=0:
        a.append(x[i])
print(*a)
