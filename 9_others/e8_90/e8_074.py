n=int(input())
s=input()
ans=0
for si in s[::-1]:
    ans*=2
    if si=='b':ans+=1
    if si=='c':ans+=2
print(ans)