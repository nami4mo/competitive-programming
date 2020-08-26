k,a,b = map(int, input().split())

if a > b-2:
    print(k+1)
else:
    if k < a-1:
        print(k+1)
    else:
        rem = k-(a-1)
        if rem%2 == 0:
            cnt = rem//2
            ans = a+(b-a)*cnt
            print(ans)
        else:
            cnt = rem//2
            ans = a+(b-a)*cnt
            ans += 1
            print(ans)