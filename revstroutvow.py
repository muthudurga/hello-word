N=int(input())
S=input()
x=['a','e','i','o','u']
y=[]
a=''
if len(S)==N:
    for i in range(N):
        if S[i] not in x:
            y.append(S[i])
    z=y[::-1]
    for i in range(len(z)):
        a=a+z[i]
    print(a)
