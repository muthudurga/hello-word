N=int(input())
a=[]
b=[]
for i in range(1,N+1):
    x=N/i
    y=int(N/i)
    if x==y:
        if i not in a:
            a.append(i)

for i in range(len(a)):
    if a[i]>1:
        for z in range(2,a[i]):
            if a[i]%z==0:
                break
        else:
            b.append(a[i])
print(*b)
