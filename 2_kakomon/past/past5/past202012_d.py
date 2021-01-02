n=int(input())
sl=[]
for _ in range(n):
    ss=input()
    s=int(ss)
    sl.append((s,-len(ss),ss))

sl.sort()
for s,_ ,ss in sl:
    print(ss)
