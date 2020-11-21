s=input()
n=len(s)
# bcnt=s.count('B')
bcnt=0
ans = 0
for i in range(n-1,-1,-1):
    if s[i] == 'B':
        d=n-1-i-bcnt
        bcnt+=1
        ans+=d
print(ans)