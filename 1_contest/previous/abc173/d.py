
def main():
    n = int(input())
    al = list(map(int, input().split()))
    al.sort(reverse=True)
    ans = 0

    for i in range(n):
        ans += al[i//2]

    ans -= al[0]
    print(ans)


if __name__ == "__main__":
    main()