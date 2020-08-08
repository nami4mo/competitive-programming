import sys
input = sys.stdin.readline

m = int(input())
keta = 0
curr_sum = 0
ten_up_cnt = 0
for _ in range(m):
    d,c = map(int, input().split())
    keta += c
    curr_sum += d*c
    ten_up_cnt += curr_sum//10
    # curr_sum%=10

# ans = keta + (curr_sum+curr_sum//10)//10 - 1
cnt = 0
for i in range(1,16):
    # print(f'---{i}')
    # print(curr_sum//(10**i))
    cnt += curr_sum//(10**i)
ans = keta + (curr_sum + cnt)//10 -1
print(ans)