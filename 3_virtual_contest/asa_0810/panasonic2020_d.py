alps = 'abcdefghijklmnopqrstuvwxyz'

def dfs(last, curr_s, sl, n):
    if len(curr_s) == n:
        sl.append(curr_s)
        return

    for i in range(0,last+2):
        s = curr_s + alps[i]
        dfs(max(last,i), s, sl, n)


def main():
    n = int(input())
    sl = []
    dfs(0, 'a', sl, n)
    for s in sl: print(s)


if __name__ == "__main__":
    main()