from itertools import product

# experiment
dp_dic = {}
def dfs(al):
    if all(a <= 1 for a in al):
        dp_dic[tuple(al)] = True
        return True
    if tuple(al) in dp_dic:
        return dp_dic[tuple(al)]
    
    ite = list(product(range(2),repeat=len(al)))
    for pattern in ite[1:]:
        c_al = al[:]
        for i, v in enumerate(pattern):
            if v == 1:
                c_al[i] = max(0,c_al[i]-1)
        c_al.sort()
        if c_al == al: continue
        res = dfs(c_al)
        if not res:
            dp_dic[tuple(al)] = True
            return True

    dp_dic[tuple(al)] = False
    return False
    

def main():
    # t = []
    # f = []
    # for i1 in range(1,10):
    #     for i2 in range(i1,10):
    #         for i3 in range(i2,10):
    #             for i4 in range(i3,10):
    #                 al = [i1,i2,i3,i4]
    #                 ans = dfs(al)
    #                 if ans: t.append(al)
    #                 else: f.append(al)

    # # print(t)
    # print(f)
    n = int(input())
    al = [int(input()) for _ in range(n)]
    ans = all(a%2 == 0 for a in al)
    if ans: print('second')
    else: print('first')

if __name__ == "__main__":
    main()