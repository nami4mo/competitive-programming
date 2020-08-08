
from itertools import product

def main():
    n,a,b,c = map(int, input().split())
    targetl = [a,b,c]
    targetl.sort()
    ll = []
    for _ in range(n):
        l = int(input())
        ll.append(l)

    ans = 10**9
    ite = product(range(4),repeat=n)
    ite = list(ite)
    for it in ite:
        bamboosl = [ [],[],[] ]
        cost = -30
        for i,v in enumerate(it):
            if v != 3:
                bamboosl[v].append(ll[i])
                cost += 10

        continue_f = False    
        for bamboos in bamboosl:
            if not bamboos: continue_f = True
        if continue_f: continue

        longs = []
        for bamboos in bamboosl:
            curr_l = sum(bamboos)
            longs.append(curr_l)
        longs.sort()

        for v1,v2 in zip(targetl,longs):
            cost += abs(v1-v2)
            
        ans = min(ans,cost)

    print(ans)


if __name__ == "__main__":
    main()