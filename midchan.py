s=input()
y=[]
for i in range(len(s)):
    y.append(s[i])
x=int(len(y)/2)
if x%2!=0:
    y[x]='*'
else:
    y[x]='*'
    y[x-1]='*'
z=''
for i in range(len(y)):
    z=z+y[i]
print(z)
