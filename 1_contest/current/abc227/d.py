ans=0

def rec(n,k,al):
    global ans
    ans+=max(rec(n-1,k-1),al[n-1])
    


def main():
    n,k=map(int, input().split())
    al=list(map(int, input().split()))



if __name__ == "__main__":
    main()