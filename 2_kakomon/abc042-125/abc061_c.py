# https://atcoder.jp/contests/arc061/tasks/arc061_a

s = str(input())
n = len(s)-1

item = [i for i in range(n)]

res = 0
for i in range(2**n):
    bag = []
    for j in range(n):
        if (i>>j) & 1:
            bag.append(item[j])

    sp = ''
    for i, keta in enumerate(s):
        sp += keta
        if i in bag: sp += '+'
    
    sl = sp.split('+')
    sl = list(map(int, sl) )
    res += sum(sl)
print(res)

# for pos in bag:
