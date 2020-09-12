def ctoi(c):
    return ord(c) - ord('a')

n,k = map(int, input().split())
s = list(input())
s_cnts = [0]*26
cnts_dict = {}

for si in s[:k]:
    s_cnts[ctoi(si)] += 1

cnts_tuple = tuple(s_cnts)
cnts_dict[cnts_tuple] = 0


for i in range(1,n-k+1):
    in_s = s[i+k-1]
    out_s = s[i-1]
    s_cnts[ctoi(in_s)] += 1
    s_cnts[ctoi(out_s)] -= 1
    cnts_tuple = tuple(s_cnts)
    if cnts_tuple in cnts_dict:
        if cnts_dict[cnts_tuple] <= i-k:
            print('YES')
            exit()
    else:
        cnts_dict[cnts_tuple] = i
else:
    print('NO')