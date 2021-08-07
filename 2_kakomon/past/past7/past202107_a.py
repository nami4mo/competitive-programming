s=input()
v=0
for i in range(len(s)-1):
    if i%2==0: v+=int(s[i])*3
    else: v+=int(s[i])
v%=10
if v==int(s[-1]):
    print('Yes')
else:
    print('No')