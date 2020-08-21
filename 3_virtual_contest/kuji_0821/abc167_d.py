n,k = map(int, input().split())
al = list(map(int, input().split()))   

cnt = 0
cl = [-1]*(n+1)
cll = [1]
curr = 1
for i in range(min(n,k)):
    # print(curr)
    next_c = al[curr-1]
    if cl[next_c] != -1:
        # loop_start = (i+1)
        loop_start = cl[next_c]
        rem = k - (i+1)
        break
    else:
        cl[next_c] = i + 1
        cll.append(next_c)
    curr = next_c

else:
    print(curr)
    exit()

# print(rem)
loop_c = cll[loop_start:]
# print(loop_c)
last_ind = rem%len(loop_c)
ans = loop_c[last_ind]
print(ans)