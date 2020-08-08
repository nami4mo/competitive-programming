import collections


def main():
    n = int(input())
    al = list(map(int, input().split()))
    al.sort()

    dp = [1]*(10**6+1) 
    for a in al:
        if dp[a] >= 0:
            dp[a] -= 1
            for i in range(2,10**6//a + 1):
                dp[a*i] -= 2
    
    ans = 0
    for a in al:
        if dp[a] >= 0: ans+=1
    print(ans)


if __name__ == "__main__":
    main()