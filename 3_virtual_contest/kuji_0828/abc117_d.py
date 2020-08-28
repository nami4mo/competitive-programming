n,k = map(int, input().split())
al = list(map(int, input().split()))

bit_cnts = [0]*41
for a in al:
    for i in range(41):
        if a&(1<<i) > 0:
            bit_cnts[i] += 1


dp_same = [0]*42
dp_small = [0]*42
small_flag = False
for i in range(41,0,-1):
    curr_bit = i-1
    kbit = 0
    if k&(1<<curr_bit) > 0: kbit = 1
    if kbit == 0:
        dp_same[i-1] = dp_same[i] + pow(2,curr_bit)*bit_cnts[curr_bit]
        if small_flag:
            dp_small[i-1] = dp_small[i] + pow(2,curr_bit)*(n-bit_cnts[curr_bit])
            dp_small[i-1] = max(dp_small[i-1], dp_small[i] + pow(2,curr_bit)*(bit_cnts[curr_bit]))
    else:
        dp_same[i-1] = dp_same[i] + pow(2,curr_bit)*(n-bit_cnts[curr_bit])
        dp_small[i-1] = dp_same[i]+pow(2,curr_bit)*(bit_cnts[curr_bit])
        if small_flag:
            dp_small[i-1] = max(dp_small[i-1], dp_small[i] + pow(2,curr_bit)*(n-bit_cnts[curr_bit]))
            dp_small[i-1] = max(dp_small[i-1], dp_small[i] + pow(2,curr_bit)*(bit_cnts[curr_bit]))
        small_flag = True

ans = max(dp_same[0],dp_small[0])
print(ans)