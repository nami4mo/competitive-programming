al=[]
for _ in range(31):
    s=input()
    ans=''
    for si in s:
        c=(ord(si)-ord('a')+13)%26
        c=chr(c+ord('a'))
        ans+=c
    al.append(ans)
print()
for a in al:print(a)