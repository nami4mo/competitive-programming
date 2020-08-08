s = list(input())

if len(s) == 2:
    if s[0] == s[1]:
        print(1,2)
    else:
        print(-1,-1)
    exit()


for i, (s1,s2,s3) in enumerate(zip(s[:-2], s[1:-1], s[2:])):
    same_cnt = 0
    if s1 == s2 or s2 == s3 or s3 == s1:
        print(i+1, i+3)
        break

else:
    print(-1,-1)
