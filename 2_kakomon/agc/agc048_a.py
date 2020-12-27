for _ in range(int(input())):
    s=input()
    if s>'atcoder':
        print(0)
        continue
    s=list(s)
    ans=0
    if s[0]!='a':
        print(0)
        continue

    if len(s)==1:
        print(-1)
        continue

    if s[1]>'t':
        print(0)
        continue
    if s[1]!='a':
        print(1)
        continue

    # aa...
    for i in range(2,len(s)):
        if s[i]>'t':
            print(i-1)
            break
        if s[i]!='a':
            print(i)
            break
    else:
        print(-1)
