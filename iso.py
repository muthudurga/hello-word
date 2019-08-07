N,M=input().split()
x={}
y=''
if len(M)==len(N):
    for i in range(len(M)):
        if N[i] not in x:
            x[N[i]]=M[i]
    for i in range(len(N)):
        y=y+x[N[i]]
    if M==y:
        print('yes')
    else:
        print('no')
        
    
