n=int(input())
ans=[]
while n>1:
    if n%2==0:
        n//=2
        ans.append('B')
    else:
        n-=1
        ans.append('A')
ans.append('A')
ans=ans[::-1]
print(''.join(ans))