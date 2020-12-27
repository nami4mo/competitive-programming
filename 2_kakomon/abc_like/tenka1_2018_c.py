from collections import deque

n=int(input())
al=[int(input()) for _ in range(n)]
al.sort(reverse=True)

if n%2==0:
    ans=0
    q=deque(al)
    double=n//2-1
    for i in range(double):
        ans += 2*q.popleft()
    ans += q.popleft()
    ans -= q.popleft()
    for i in range(double):
        ans -= 2*q.popleft()
    print(ans)

else:
    ans1=0
    q=deque(al)
    dp=n//2
    dm=n//2-1
    for i in range(dp):
        ans1 += 2*q.popleft()
    ans1 -= q.popleft()
    ans1 -= q.popleft()
    for i in range(dm):
        ans1 -= 2*q.popleft()

    ans2=0
    q=deque(al)
    dp=n//2-1
    dm=n//2
    for i in range(dp):
        ans2 += 2*q.popleft()
    ans2 += q.popleft()
    ans2 += q.popleft()
    for i in range(dm):
        ans2 -= 2*q.popleft()
    print(max(ans1,ans2))