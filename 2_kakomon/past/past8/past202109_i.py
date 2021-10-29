
def main():
    n=int(input())
    al=list(map(int, input().split()))
    cnt=0
    for i in range(n):
        while al[i]%2==0:
            al[i]//=2
            cnt+=1
    from heapq import heappop, heappush, heapify
    heapify(al)
    for _ in range(cnt):
        poped=heappop(al)
        heappush(al,poped*3)
    print(heappop(al))


if __name__ == '__main__':
    main()