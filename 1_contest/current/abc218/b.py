alps = 'abcdefghijklmnopqrstuvwxyz'  # string.ascii_lowercase
pl=list(map(int, input().split()))
ans=''
for p in pl:
    ans+=alps[p-1]
print(ans)