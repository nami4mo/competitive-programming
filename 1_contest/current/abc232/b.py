def conv(c, i):
    v = ord(c)-ord('a')
    v += i
    v %= 26
    od = ord('a')+v
    return chr(od)


# print(conv('c', 5))

s = list(input())
t = list(input())


for i in range(26):
    ss = []
    for si in s:
        ss.append(conv(si, i))
    if ss == t:
        print('Yes')
        exit()
print('No')
