n=int(input())
al=list(map(int, input().split()))
bl=[(b,i+1) for i,b in enumerate(al)]
bl.sort(reverse=True)
# print(bl)
print(bl[1][1])