n = int(input())
s = input()
t = input()

for i in range(n):
    if s[i:] == t[:n-i]:
        ans = (n-i) + i*2
        print(ans)
        break
else:
    print(n*2)