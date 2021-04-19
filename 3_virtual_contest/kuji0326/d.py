s=input()
sl=list(s)
sl=list(set(sl))

ans=10**10
for si in s:
    ll=s.split(si)
    dist=0
    for l in ll:
        dist=max(dist, len(l))
    ans=min(ans,dist)
print(ans)
    # curr_s=s
#     new_s=''
#     for cnt in range(len(s)):
#         flag=True
#         for i in range(len(curr_s)-1):
#             if curr_s[i]==si or curr_s[i+1]==si:
#                 new_s+=si
#             else:
#                 new_s+='.'
#                 flag=False
#         curr_s=new_s
#         if flag:
#             ans=min(cnt+1,ans)
# print(ans)