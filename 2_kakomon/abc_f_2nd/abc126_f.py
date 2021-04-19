m,k=map(int, input().split())
if pow(2,m)-1<k:
    print(-1)
    exit()

if m==1:
    if k==0:
        print('0 0 1 1')
    else:
        print(-1)
    exit()

al=[]
for i in range(pow(2,m)-1,-1,-1):
    if i!=k:al.append(i)
al.append(k)
for i in range(pow(2,m)):
    if i!=k:al.append(i)
al.append(k)
print(*al)