# m,n,N=map(int, input().split())
# ans=N
# rem=N
# while rem>=m:
#     cnt=(rem//m)*n
#     ans+=cnt
#     rem=rem%m+cnt
# print(ans)

for i in range(10**5):
    c=0
    for j in range(i,10**5):
        if c>100:break
        c+=1