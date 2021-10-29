x=input()
alps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # string.ascii_lowercase

n=int(input())
sl=[input() for _ in range(n)]
ssl=[]
for s in sl:
    ss=s
    for i in range(26):
        ss=ss.replace(x[i],alps[i])
    ssl.append(ss)

ssl.sort()

for ss in ssl:
    s=ss
    for i in range(26):
        s=s.replace(alps[i],x[i])
    print(s)