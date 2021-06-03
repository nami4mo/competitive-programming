s=input()
s=s[::-1]
ans=''
for si in s:
    if si=='6':ans+='9'
    elif si=='9': ans+='6'
    else: ans+=si
print(ans)