ss=input()
s=list(ss)
if ss=='a' or ss=='zzzzzzzzzzzzzzzzzzzz':
    print('NO')
    exit()

n=len(s)
for i in range(n):
    for j in range(n):
        if s[i]!=s[j]:
            s[i],s[j]=s[j],s[i]
            print(''.join(s))
            exit()

if s[0]=='z':
    ans=s[:-1]+['a','y']
    print(''.join(ans))
    exit()

if n==1:
    ans='a'+chr(ord(s[0])-1)
    print(ans)
    exit()

v=0
for si in s:
    v+=(ord(si)-ord('a')+1)

ans=''
while v>0:
    if v>26:
        ans+='z'
        v-=26
    else:
        ans+=chr(ord('a')+(v-1))
        break
print(ans)