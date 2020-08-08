import sys
sys.setrecursionlimit(10**6)


def dfs(curr_num, e753, list753, n):
    if curr_num > n: return
    if e753 == 7:
        list753.append(curr_num)
    dfs(curr_num*10+7, e753|4, list753, n)
    dfs(curr_num*10+5, e753|2, list753, n)
    dfs(curr_num*10+3, e753|1, list753, n)


def main():
    n = int(input())
    list753 = []
    dfs(0,0,list753,n)
    print(len(list753))


if __name__ == "__main__":
    main()