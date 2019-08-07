N=int(input())
a=[]
for i in range(1,N+1):
    x=N/i
    y=int(N/i)
    if x==y:
        if i not in a:
            a.append(i)
print(*a)
    
    
