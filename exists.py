N,K=input().split()
x=[int(x) for x in input().split()]
if len(x)==int(N):
    if int(K) in x:
        print('yes')
    else:
        print('no')
