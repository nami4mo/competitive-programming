
def main():
    n = int(input())
    al = []
    for _ in range(n):
        al.append(list(input()) )


    f_s = ''
    center = ''

    for i in range(n):
        front = i
        back = n-1-i
        if front > back:
            break
        elif front == back:
            center = al[front][0]
        else:
            common = set(al[front]) & set(al[back])
            common = list(common)
            if len(common) == 0:
                print(-1)
                return
            else:
                f_s += common[0]

    ans = f_s + center + f_s[::-1]
    print(ans)

if __name__ == "__main__":
    main()