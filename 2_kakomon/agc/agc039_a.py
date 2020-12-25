s=list(input())
n=len(s)
k=int(input())


if all([si == s[0] for si in s]):
    cnt=n*k
    print(cnt//2)

elif s[0]!=s[-1]:
    ans=0
    for i in range(1,n):
        if s[i]==s[i-1]:
            s[i]='.'
            ans+=1
    print(ans*k)

else:
    top=0
    bottom=0
    for i in range(n):
        if s[i]!=s[0]:
            break
        top+=1

    for i in range(n-1,-1,-1):
        if s[i]!=s[0]:
            break
        bottom+=1
    
    s=s[top:n-bottom]
    # print(s)
    ans=0
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            s[i]='.'
            ans+=1
    ans=ans*k
    # print(ans)
    ans += (bottom//2 + top//2 + ((top+bottom)//2)*(k-1))
    print(ans)
