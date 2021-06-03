n,k=map(int, input().split())
t=input()
d={'J':'j','O':'o','I':'i','j':'J','o':'O','i':'I'}
ans=''
for i in range(n):
    if i+1>=k: ans+=d[t[i]]
    else:ans+=t[i]
print(ans)