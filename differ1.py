n,m=input().split()
s=0
if len(n)==len(m):
    for i in range(len(n)):
        if n[i]!=m[i]:
            s=s+1
    if s==1:
        print('yes')
    else:
        print('no')
