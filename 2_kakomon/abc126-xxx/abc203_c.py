import sys
input = sys.stdin.readline
n,k=map(int, input().split())
abl=[]
for _ in range(n):
    a,b=map(int, input().split())
    abl.append((a,b))

abl.sort(key=lambda x:x[0])
pos=0
for a,b in abl:
    if a-pos>k:
        print(pos+k)
        exit()
    k-=(a-pos)
    pos=a
    k+=b

print(pos+k)