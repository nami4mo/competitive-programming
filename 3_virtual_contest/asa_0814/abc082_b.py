s =input()
t = input()
s = sorted(s, key=str.lower)
t = sorted(t, key=str.lower, reverse=True)
s = ''.join(s)
t = ''.join(t)
l = [s,t]
l.sort()
if l[0] == s and s != t:
    print('Yes')
else:
    print('No')