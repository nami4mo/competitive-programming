n = int(input())
al = input()

cntl = []
prev = al[0]
cnt = 1
for a in al[1:]:
    if prev == a: cnt+=1
    else:
        cntl.append((prev,cnt))
        cnt = 1
        prev = a
cntl.append((prev,cnt))

ansx = 0
ansy = 0
if cntl[0][0] == '.':
    ansx += cntl[0][1]
if cntl[-1][0] == '.':
    ansy += cntl[-1][1]

for c,v in cntl:
    if c == '.' and v > ansx+ansy:
        ansx += (v-ansx-ansy)

print(ansx,ansy)