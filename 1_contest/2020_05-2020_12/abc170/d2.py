

import collections
import math

def get_sieve_of_eratosthenes_new(data):
    prime = []
    limit = max(data) // 2 + 1
    # data = [i + 1 for i in range(1, n)]
    while data:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]
    return prime + data

def main():
    n = int(input())
    al = list(map(int, input().split()))
    al_not_multi = []
    cnt = collections.Counter(al)
    for i,v in cnt.items():
        if v == 1:
            al_not_multi.append(i)

    if not al_not_multi:
        print(0)
        return

    al_not_multi.sort()

    ans = get_sieve_of_eratosthenes_new(al_not_multi)
    print(len(ans))

    # ans = 0
    # lim = int(al_not_multi[-1]//2 + 1)
    # while al_not_multi:
    #     p = al_not_multi[0]
    #     if p > lim:
    #         break
    #     al_not_multi = [e for e in al_not_multi[1:] if e % p != 0]
    #     ans += 1


    # al_n = al_not_multi[:]
    # ans = 0
    # while al_n:
    #     new_al_n = []
    #     start = al_n[0]
    #     for a in al_n[1:]:
    #         if a%start!=0:
    #             new_al_n.append(a)
    #     al_n = new_al_n[:]
    #     ans += 1
    # print(ans)




if __name__ == "__main__":
    main()