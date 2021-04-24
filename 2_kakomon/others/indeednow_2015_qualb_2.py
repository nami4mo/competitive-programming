s=input()
t=input()

if s==t:
    print(0)
    exit()
for i in range(len(s)):
    s=s[-1]+s[:-1]
    if s==t:
        print(i+1)
        exit()
print(-1)