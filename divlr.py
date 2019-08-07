L,R=input().split()
x=int(L)
y=int(R)
if max(x,y)%min(x,y)==0:
    print(max(x,y))
else:
    print(x*y)
