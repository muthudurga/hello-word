L,R=input().split()
x=int(L)
y=int(R)
if max(x,y)%min(x,y)==0:
    print(max(x,y))
else:
    for i in range(1,min(x,y)):
        if (max(x,y)*i)%min(x,y)==0:
            print(max(x,y)*i)
            break
