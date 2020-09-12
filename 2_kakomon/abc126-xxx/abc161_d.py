def dfs(lls, curr_num, lim):
    if curr_num > lim: return
    lls.append(curr_num)
    last_num = int(str(curr_num)[-1])
    if last_num > 0:
        dfs(lls, curr_num*10+last_num-1, lim)
    if last_num < 9:
        dfs(lls, curr_num*10+last_num+1, lim)
    dfs(lls, curr_num*10+last_num, lim)


def main():
    k = int(input())
    lls = []
    for i in range(1,10):
        dfs(lls, i, 3234566668)

    lls.sort()
    print(lls[k-1])
    


if __name__ == "__main__":
    main()