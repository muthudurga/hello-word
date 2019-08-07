l,r=input().split()
a=[]
for i in range(int(l),int(r)+1):
    if i>1:
        for x in range(2,i):
            if i%x==0:
                break
        else:
            a.append(i)
print(len(a))
