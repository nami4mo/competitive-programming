'''
    2d-imos
'''

MAX=1010
n=int(input())
imos=[[0]*MAX for _ in range(MAX)]
for _ in range(n):
    x1,y1,x2,y2=map(int, input().split())
    imos[x1][y1]+=1
    imos[x2][y2]+=1
    imos[x1][y2]-=1
    imos[x2][y1]-=1
for x in range(MAX):
    for y in range(1,MAX):
        imos[x][y]+=imos[x][y-1]

for y in range(MAX):
    for x in range(1,MAX):
        imos[x][y]+=imos[x-1][y]

ans=[0]*(n+1)
for x in range(MAX):
    for y in range(MAX):
        if imos[x][y]<0:continue
        ans[imos[x][y]]+=1

for i in range(1,n+1):
    print(ans[i])