def main():
    s = input()
    rem_l = [0]*2019
    rem_l[0] = 1
    curr_rem = 0
    for i, s_i in enumerate(s[::-1]):
        num = int(s_i)
        curr_rem = (curr_rem + num*pow(10,i))%2019
        rem_l[curr_rem] += 1

    ans = 0
    for r in rem_l:
        ans += r*(r-1)//2

    print(ans)

if __name__ == "__main__":
    main()