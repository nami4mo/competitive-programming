n=int(input())
s=input()
t=input()

s0=[]
t0=[]
for i in range(n):
    if s[i]=='0':s0.append(i)
    if t[i]=='0':t0.append(i)

if len(s0)!=len(t0):
    print(-1)
    exit()

# print(s0,t0)
ans=0
for a,b in zip(s0,t0):
    if a!=b:ans+=1
print(ans)