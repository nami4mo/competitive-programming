n,m=map(int, input().split())
s=input()
t=input()

lefts=[]
sind=0
for ti in t:
    while True:
        if ti==s[sind]:
            lefts.append(sind)
            sind+=1
            break
        sind+=1

rights=[]
sind=n-1
for ti in t[::-1]:
    while True:
        if ti==s[sind]:
            rights.append(sind)
            sind-=1
            break
        sind-=1
rights=rights[::-1]

ans=0
for i in range(m-1):
    d=rights[i+1]-lefts[i]
    ans=max(ans,d)

print(ans)
