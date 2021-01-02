from heapq import heapify, heappop, heappush

def update(dp,num,val):
    if not num in dp: 
        dp[num]=val
        return True
    else:
        dp[num]=min(dp[num],val)
        return True

ansl=[]
for _ in range(int(input())):
    n,a,b,c,d=map(int, input().split())
    dp={}
    dp[n]=0
    dp[0]=10**20
    q=[]
    st=set()
    heappush(q,-n)
    st.add(n)
    while q:
        poped=heappop(q)
        poped*=(-1)
        # if poped<=10:
        #     st.remove(poped)
        if poped <= 1: continue
        if poped%2==0: 
            num=poped//2
            update(dp,num,dp[poped]+a)
            if not num in st:
                st.add(num)
                heappush(q,-num)
        else:
            rem=poped%2
            num0=(poped-rem)//2
            update(dp,num0,dp[poped]+d*rem+a)
            if not num0 in st:
                st.add(num0)
                heappush(q,-num0)
            num1=(poped+(2-rem))//2
            update(dp,num1,dp[poped]+d*(2-rem)+a)
            if not num1 in st:
                st.add(num1)
                heappush(q,-num1)

        if poped%3==0: 
            num=poped//3
            update(dp,num,dp[poped]+b)
            if not num in st:
                st.add(num)
                heappush(q,-num)
        else:
            rem=poped%3
            num0=(poped-rem)//3
            update(dp,num0,dp[poped]+d*rem+b)
            if not num0 in st:
                st.add(num0)
                heappush(q,-num0)
            num1=(poped+(3-rem))//3
            update(dp,num1,dp[poped]+d*(3-rem)+b)
            if not num1 in st:
                st.add(num1)
                heappush(q,-num1)

        if poped%5==0: 
            num=poped//5
            update(dp,num,dp[poped]+c)
            if not num in st:
                st.add(num)
                heappush(q,-num)
        else:
            rem=poped%5
            num0=(poped-rem)//5
            update(dp,num0,dp[poped]+d*rem+c)
            if not num0 in st:
                st.add(num0)
                heappush(q,-num0)
            num1=(poped+(5-rem))//5
            update(dp,num1,dp[poped]+d*(5-rem)+c)
            if not num1 in st:
                st.add(num1)
                heappush(q,-num1)

        update(dp,0,dp[poped]+d*poped)

    ansl.append(min(dp[0],dp[1]+d))
for a in ansl:print(a)