n,x=map(int, input().split())
al=list(map(int, input().split()))
bl=[]
for a in al:
    if a!=x:
        bl.append(a)

print(*bl)