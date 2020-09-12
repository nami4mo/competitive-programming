s = input()
a,b,c,d = map(int, input().split())

sa = s[0:a]
sb = s[a:b]
sc = s[b:c]
sd = s[c:d]
se = s[d:]

ans = sa + '"' + sb+ '"' + sc + '"' + sd + '"' + se
print(ans)

