def nums(num):
    res_cnt = (10-1)//num +1
    res_val = num*res_cnt-9
    return res_cnt, res_val

def solve(m,dcl):
    rems=[]
    ans=0
    for d,c in dcl:
        if d==0:
            ans+=c
            continue
        c_cnt, c_val = c, d
        while True:
            needed_cnt, next_val = nums(c_val)

            if c_cnt < needed_cnt:break
            loops = c_cnt//needed_cnt
            rem_cnt = c_cnt%needed_cnt

            if rem_cnt > 0:
                rems.append(c_val*rem_cnt)
                ans+=(rem_cnt-1)

            c_cnt = loops
            c_val = next_val
            ans += needed_cnt*loops

        for _ in range(c_cnt):
            rems.append(c_val)
    # print(rems)

    if len(rems) <= 1:
        return ans

    cv = rems[0]
    for r in rems[1:]:
        ans+=1
        cv+=r
        if cv>=10:
            ans+=1
            cv-=9
        
    return ans

def solve2(m,dcl):
    rems = []
    for d,c in dcl:
        for _ in range(c):
            rems.append(d)
    cv = rems[0]
    ans=0
    for r in rems[1:]:
        ans+=1
        cv+=r
        if cv>=10:
            ans+=1
            cv-=9 
    return ans

from random import randint
if __name__ == "__main__":
    m=int(input())
    dcl=[]
    for _ in range(m):
        d,c=map(int, input().split())
        dcl.append((d,c))
    ans = solve(m,dcl)
    print(ans)

    # for _ in range(1000):
    #     m = randint(3,6)
    #     dcl = []
    #     for i in range(m):
    #         d=randint(1,9)
    #         c=randint(1,5)
    #         dcl.append((d,c))
    #     ans=solve(m,dcl)
    #     ans2=solve2(m,dcl)
    #     if ans!=ans2:
    #         print('----')
    #         print(m)
    #         print(dcl)
    #         print('ans1',ans)
    #         print('ans2',ans2)