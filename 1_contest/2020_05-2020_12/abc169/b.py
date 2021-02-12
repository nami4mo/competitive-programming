def main():
    n = int(input())
    al = list(map(int, input().split())) 
    if 0 in al:
        print(0)
        return
        
    INF = 10**18
    curr_ans = 1
    for a in al:
        curr_ans*=a
        if curr_ans > INF:
            curr_ans = -1
            break

    print(curr_ans)

if __name__ == "__main__":
    main()