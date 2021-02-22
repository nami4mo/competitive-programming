# for a in range(1,50):
#     for b in range(1,50):
#         left=(a//b)
#         right=a%b
#         if left==right:
#             print(a,b)

al=[]
for _ in range(int(input())):
    x,y=map(int, input().split())
    ans=0
    for r in range(1,x):
        if r*r>=x:break
        cmin=r+2
        cmax=min(x//r,y+1)
        cnt=cmax-cmin+1
        ans+=max(0,cnt)
    al.append(ans)
for a in al:print(a)