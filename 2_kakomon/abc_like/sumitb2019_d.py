n = int(input())
s = input()
cnt = 0
for s1 in range(10):
    s1_ind = s.find(str(s1))
    if s1_ind == -1 or s1_ind >= len(s)-2 : continue
    for s2 in range(10):
        s2_ind = s[s1_ind+1: ].find(str(s2)) + s1_ind + 1
        if s2_ind <= s1_ind or s2_ind >= len(s)-1: continue
        for s3 in range(10):
            s3_ind = s[s2_ind+1: ].find(str(s3)) + s2_ind + 1
            if s3_ind > s2_ind: 
                cnt+=1

print(cnt)

