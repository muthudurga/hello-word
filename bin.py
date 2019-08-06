S=input()
a=[]
b=[]
for i in range(len(S)):
    if S[i]=='0' or S[i]=='1':
        a.append(S[i])
    else:
        b.append(S[i])
if b==[]:
    print('yes')
else:
    print('no')
