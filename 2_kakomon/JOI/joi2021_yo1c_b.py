n=int(input())
s=input()
ans=0
for i,si in enumerate(s):
    if i%2==0 and si!='I':ans+=1
    if i%2==1 and si!='O':ans+=1
print(ans)