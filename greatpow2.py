N=int(input())
for i in range(N+1):
    x=2**i
    if x>N:
        print(x)
        break
