import sys
input = sys.stdin.readline

for _ in range(int(input())):
    ca,cb = map(int, input().split())
    al = list(input().rstrip())

    cntl = []
    prev = al[0]
    cnt = 1
    for a in al[1:]:
        if prev == a: cnt+=1
        else:
            cntl.append((prev,cnt))
            cnt = 1
            prev = a
    cntl.append((prev,cnt))
    if cntl[0][0] == '0': 
        if len(cntl) == 1:
            print(0)
            continue
        cntl = cntl[1:]
    
    if cntl[-1][0] == '0':
        cntl = cntl[:-1]
    
    # print(cntl)
    cost = ca*(len(cntl)+1)//2
    # print(cost,'-')
    for i in range(len(cntl)//2):
        d = cntl[1+i*2][1]
        dc = d*cb
        if dc < ca:
            cost -= (ca-dc)
    print(cost)
