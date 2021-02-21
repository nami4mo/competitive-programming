def ctoi(c):
    return ord(c)-ord('a')

s=input()
n=len(s)
alps = 'abcdefghijklmnopqrstuvwxyz' # string.ascii_lowercase

# last_is=[-1]*26
last_cnts = {chr(ord('a') + i): 0 for i in range(26)}
last_cnts[s[-1]]=1
ans=0
for i in range(n-1,0,-1):
    # print(last_is)
    si=s[i]
    if s[i]==s[i-1]:
        # print('aaa')
        dist=n-i-1-last_cnts[si]
        ans+=max(dist,0)
        # print(dist)
        last_cnts = {chr(ord('a') + j): 0 for j in range(26)}
        last_cnts[si]=n-i
    else:
        last_cnts[si]+=1
    
print(ans)
