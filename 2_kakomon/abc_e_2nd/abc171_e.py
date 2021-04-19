n=int(input())
al=list(map(int, input().split()))
asum=0
for a in al:
    asum^=a
for a in al:
    print(asum^a)
