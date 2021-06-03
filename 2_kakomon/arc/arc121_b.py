n=int(input())
rl,gl,bl=[],[],[]
for _ in range(2*n):
    a,c=map(str, input().split())
    a=int(a)
    if c=='R':rl.append(a)
    if c=='G':gl.append(a)
    if c=='B':bl.append(a)

rl.sort()
bl.sort()
gl.sort()

if len(rl)%2==0  and len(gl)%2==0 and len(bl)%2==0:
    print(0)
    exit()

if len(rl)%2==0:
    evens=rl
    os1=gl
    os2=bl

if len(gl)%2==0:
    evens=gl
    os1=rl
    os2=bl

if len(bl)%2==0:
    evens=bl
    os1=gl
    os2=rl

from bisect import bisect_left, bisect_right
ans=10**18
for v in os1:
    ind1 = bisect_right(os2, v) - 1
    ind1 = ind1 if 0 <= ind1 < len(os2) else None        # -> 7
    val1 = os2[ind1] if ind1 is not None else None  # -> 6
    if val1 is not None:
        ans=min(ans,abs(val1-v))

    ind1 = bisect_left(os2, v) 
    ind1 = ind1 if 0 <= ind1 < len(os2) else None        # -> 7
    val1 = os2[ind1] if ind1 is not None else None  # -> 6
    if val1 is not None:
        ans=min(ans,abs(val1-v))

ans1=10**18
ans2=10**18
for v in evens:
    ind1 = bisect_right(os1, v) - 1
    ind1 = ind1 if 0 <= ind1 < len(os1) else None        # -> 7
    val1 = os1[ind1] if ind1 is not None else None  # -> 6
    if val1 is not None:
        ans1=min(ans1,abs(val1-v))

    ind1 = bisect_left(os1, v) 
    ind1 = ind1 if 0 <= ind1 < len(os1) else None        # -> 7
    val1 = os1[ind1] if ind1 is not None else None  # -> 6
    if val1 is not None:
        ans1=min(ans1,abs(val1-v))

    ind1 = bisect_right(os2, v) - 1
    ind1 = ind1 if 0 <= ind1 < len(os2) else None        # -> 7
    val1 = os2[ind1] if ind1 is not None else None  # -> 6
    if val1 is not None:
        ans2=min(ans2,abs(val1-v))

    ind1 = bisect_left(os2, v) 
    ind1 = ind1 if 0 <= ind1 < len(os2) else None        # -> 7
    val1 = os2[ind1] if ind1 is not None else None  # -> 6
    if val1 is not None:
        ans2=min(ans2,abs(val1-v))

# print(ans1,ans2)

ans=min(ans, ans1+ans2)
print(ans)