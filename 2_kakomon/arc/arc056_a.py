a,b,k,l=map(int, input().split())
if a*l<=b:
    print(a*k)
else:
    st=k//l
    ans=st*b
    rem=k%l
    ans+=min(rem*a,b)
    print(ans)