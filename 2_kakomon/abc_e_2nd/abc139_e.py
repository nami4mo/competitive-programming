n=int(input())

from collections import deque
ql=[deque() for _ in range(n)]
for i in range(n):
    row=list(map(int, input().split()))
    for v in row:
        ql[i].append(v-1)

ans=0
cnt=0
cands=list(range(n))
while True:
    ans+=1
    flag=False
    st=set()
    new_cands=[]
    # print('------',ans)
    # for i in range(n):
    for i in cands:
        if not ql[i]: continue
        if i in st: continue
        cand=ql[i][0]
        if ql[cand][0]==i and (cand not in st):
            cnt+=1
            ql[i].popleft()
            ql[cand].popleft()
            flag=True
            st.add(i)
            st.add(cand)
            new_cands.append(i)
            new_cands.append(cand)
            # print(i+1,cand+1)
    cands=new_cands[:]
    if cnt==n*(n-1)//2:
        break
    if not flag:
        print(-1)
        exit()
print(ans)