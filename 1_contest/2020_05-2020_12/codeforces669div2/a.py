for _ in range(int(input())):
    n = int(input())
    al = list(map(int, input().split()))
    # ans1 = []
    # ans2 = []
    ans = []
    one_ok = False
    i = 0
    while i < n:
        if al[i] == 0:
            ans.append(0)
            i+=1
        else:
            ok = False
            for j in range(i+1,n):
                if al[j] == 1:
                    diff = j-i-1
                    ok = True
                    break
                    
            if ok:
                ans.append(1)
                if diff%2 == 0:
                    for k in range(diff):
                        ans.append(0)
                else:
                    for k in range(diff-1):
                        ans.append(0)
                ans.append(1)
            else:
                for j in range(i+1,n):
                    if al[j] == 0: ans.append(0)
                break
            i = j+1
    print(len(ans))
    print(*ans)