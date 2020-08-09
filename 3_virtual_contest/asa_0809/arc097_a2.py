s = input()
k = int(input())
n = len(s)

ss = set()
for i in range(n):
    for j in range(5):
        if i+j < n:
            ss.add(s[i:i+j+1])

sl = list(ss)
sl.sort()
print(sl[k-1])