

def main():
    n, m = map(int, input().split())
    al = list(map(int, input().split()))
    bl = list(map(int, input().split()))
    ans = 10**18
    for i in range(n):
        da = al[0]+bl[i]
        da %= m
        db = al[i]+bl[n-1]
        db %= m
        ans = min(ans, da+db)
    ans = min(ans, (al[0]+bl[n-1]) % m)
    print(ans)


if __name__ == "__main__":
    main()
