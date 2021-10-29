
from collections import deque
def main():
    n=int(input())
    s=input()
    q1=deque()
    q0=deque()
    for i in range(n):
        if s[i]=='1':q1.append(i+1)
        else:q0.append(i+1)
    if len(q0)==1:
        print(-1)
        return
    ans=[]
    if len(q0)!=0:
        v=q0.popleft()
        q0.append(v)

    for i in range(n):
        if s[i]=='1':
            ans.append(q1.popleft())
        else:
            ans.append(q0.popleft())
    print(*ans)

if __name__ == '__main__':
    main()