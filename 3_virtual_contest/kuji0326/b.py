s=input()
t=input()
n=len(s)


for _ in range(n+1):
    s=s[1:]+s[0] 
    if s==t:
        print('Yes')
        exit()
print('No')