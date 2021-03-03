from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline
def solve(al,bl):
    n=len(al)
    bst=set(bl)
    alreadys=[]
    cnts_i=[0]
    for a in al:
        if a in bst:alreadys.append(a)

    for i,a in enumerate(al):
        cnts_i.append(a-i)

    ans=0
    for left in bl:
        cnt=bisect_right(cnts_i, left)-1
        right=left+cnt-1
        sp_cnt=bisect_right(bl,right)-bisect_left(bl,left)
        already_cnt=(len(alreadys)-bisect_right(alreadys,right))
        ans=max(ans, sp_cnt+already_cnt)
    return ans

ansl=[]
for _ in range(int(input())):
    n,m=map(int, input().split())
    al=list(map(int, input().split()))
    bl=list(map(int, input().split()))
    aln,alp,bln,blp=[],[],[],[]
    for a in al:
        if a>0: alp.append(a)
        else: aln.append(-a)
    for b in bl:
        if b>0: blp.append(b)
        else: bln.append(-b)
    ans=solve(alp,blp)+solve(aln[::-1],bln[::-1])
    ansl.append(ans)

for a in ansl:print(a)