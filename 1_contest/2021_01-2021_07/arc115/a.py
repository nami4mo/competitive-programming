n,m=map(int, input().split())
cl=[0]*2
for _ in range(n):
    s=input()
    cl[s.count('1')%2]+=1

print(cl[0]*cl[1])