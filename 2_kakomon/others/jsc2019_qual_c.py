n=int(input())
s=input()

MOD=10**9+7
al=[]
for i in range(2*n):
    si=s[i]
    if i==0:
        if si=='W':
            print(0)
            exit()
        else:
            # l+=1
            al.append(1)
    else:
        sii=s[i-1]
        if sii==si:
            al.append(al[-1]*(-1))
        else:
            al.append(al[-1])

# print(al)
l=0
ans=1
for a in al:
    if a==1:
        l+=1
    else:
        ans*=l
        l-=1
        
        ans%=MOD

if l!=0:
    print(0)
    exit()
for i in range(1,n+1):
    ans*=i
    ans%=MOD
print(ans) 
