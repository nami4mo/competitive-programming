

def main():
    INF=10**8
    n=int(input())
    x,y=map(int, input().split())
    abl=[]
    for _ in range(n):
        a,b=map(int, input().split())
        abl.append((a,b))
    dp=[[INF]*(y+1) for _ in range(x+1)]
    dp[0][0]=0
    for i in range(n):
        a,b=abl[i]
        new_dp=[[INF]*(y+1) for _ in range(x+1)]
        for j in range(x+1):
            for k in range(y+1):
                new_dp[j][k]=min(new_dp[j][k], dp[j][k])
                new_dp[ min(x,j+a) ][ min(y,k+b)] = min(new_dp[ min(x,j+a) ][ min(y,k+b)], dp[j][k]+1)
        for j in range(x+1):
            for k in range(y+1):
                dp[j][k]=new_dp[j][k]

    ans=new_dp[x][y]
    if ans>=INF:ans=-1
    print(ans)


if __name__ == "__main__":
    main()