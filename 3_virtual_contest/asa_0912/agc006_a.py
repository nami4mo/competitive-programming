n=int(input())
s=input()
t=input()
for i in range(n):
    if s[i:] == t[:n-i]:
        ans = 2*i+(n-i)
        print(ans)
        break
else:
    print(n*2)