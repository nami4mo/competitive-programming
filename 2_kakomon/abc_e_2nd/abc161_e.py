n,k,c=map(int, input().split())
s=input()
l=[-1]*n
r=[-1]*n
ng=0
cnt=0
for i in range(n):
    if s[i]=='o' and ng<=0:
        cnt+=1
        l[i]=cnt
        ng=c
    else:
        ng-=1
# print(l)
if cnt>=k+2:
    exit()

ng=0
for i in range(n):
    ind=n-i-1
    if s[ind]=='o' and ng<=0:
        r[ind]=cnt
        cnt-=1
        ng=c
    else:
        ng-=1
# print(r)

for i in range(n):
    if l[i]==r[i] and l[i]>0:
        print(i+1)