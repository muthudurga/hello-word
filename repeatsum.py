N,K=input().split()
x=[int(x) for x in input().split()]
s=0
if len(x)==int(N):
    for i in range(len(x)):
        if x[i]==int(K):
            s=s+1
    print(s)
