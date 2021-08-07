s=input()
l,r=map(int, input().split())
if s[0]=='0' and len(s)>1:
    print('No')
    exit()

if len(s)>18:
    print('No')
    exit()

s=int(s)
if l<=s<=r:
    print('Yes')
else:
    print('No')