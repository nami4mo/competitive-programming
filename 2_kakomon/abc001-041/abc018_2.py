s=list(input())
n=int(input())
for _ in range(n):
    l,r=map(int, input().split())
    l-=1
    r-=1
    s=s[:l]+list(reversed(s[l:r+1]))+s[r+1:]
print(''.join(s))