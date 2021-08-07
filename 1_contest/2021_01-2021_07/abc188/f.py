from heapq import heapify, heappop, heappush

def update(dp,num,val):
    if not num in dp: 
        dp[num]=val
        return True
    else:
        dp[num]=min(dp[num],val)
        return True


x,y=map(int, input().split())
if x>=y:
    print(x-y)
else:
    dp={}
    dp[x]=10**20
    dp[x+1]=10**20
    dp[x-1]=10**20
    dp[y]=0
    q=[]
    st=set()
    heappush(q,-y)
    st.add(y)
    while q:
        poped=heappop(q)
        poped*=(-1)
        if poped <= x-3: continue
        if poped%2==0: 
            num=poped//2
            update(dp,num,dp[poped]+1)
            if not num in st:
                st.add(num)
                heappush(q,-num)
        else:
            rem=poped%2
            num0=(poped-1)//2
            update(dp,num0,dp[poped]+1+1)
            if not num0 in st:
                st.add(num0)
                heappush(q,-num0)
            num1=(poped+1)//2
            update(dp,num1,dp[poped]+1+1)
            if not num1 in st:
                st.add(num1)
                heappush(q,-num1)

        update(dp,x,dp[poped]+1*abs(poped-x))

    ans = min(dp[x],dp[x+1]+1,dp[x-1]+1)
    print(ans)

