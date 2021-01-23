s=input()
chunks=s.split('+')
ans=0
for chunk in chunks:
    if '0' not in chunk:ans+=1
print(ans)