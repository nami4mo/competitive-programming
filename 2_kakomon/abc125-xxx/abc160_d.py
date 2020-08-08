def main():
    n, x, y = map(int, input().split()) 

    ans = [0] * n
    for i in range(1,n):
        for j in range(i+1, n+1):
            r1 = j-i
            r2 = abs(x-i) + 1 + abs(j-y)
            r3 = abs(y-i) + 1 + abs(j-x)
            ans[min(r1,r2,r3)] += 1

    for i in range(1,n):
        print(ans[i])

if __name__ == "__main__":
    main()