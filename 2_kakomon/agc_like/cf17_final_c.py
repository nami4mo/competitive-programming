from itertools import product

def solve(n,dl):
    if 0 in dl:
        return 0

    doubles = []
    dl1 = []
    dl2 = []
    for i in range(1,13):
        i_cnt = dl.count(i)
        if i_cnt > 2:
            return 0
        elif i_cnt == 2:
            dl2.append(24-i)
            dl2.append(i)
        elif i_cnt == 1:
            dl1.append(i)        

    ans = 0
    ite = list(product(range(2),repeat=len(dl1)))
    for pattern in ite:
        dl24 = [0,24]
        for i, v in enumerate(pattern):
            if v == 1:
                dl24.append(24-dl1[i])
            else:
                dl24.append(dl1[i])
        dl24 = dl24 + dl2
        dl24.sort()
        diff_min = 24
        # print(dl24)
        if len(dl24) == 1:
            ans = max(ans, min(dl24[0], 24-dl24[0]))
        else:
            for a,b in zip(dl24[:-1],dl24[1:]):
                diff = b-a
                if diff != 24:
                    diff_min = min(diff_min,diff)
            ans = max(diff_min,ans)
    return ans


if __name__ == "__main__":
    n = int(input())
    dl = list(map(int, input().split()))
    ans = solve(n,dl)
    print(ans)