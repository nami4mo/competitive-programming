

def main():
    n = int(input())
    al = list(map(int, input().split()))
    all_xor = 0
    for a in al:
        all_xor = all_xor ^ a

    ans = []
    for a in al:
        curr_ans = all_xor ^ a
        ans.append(curr_ans)

    print(*ans)


if __name__ == "__main__":
    main()


