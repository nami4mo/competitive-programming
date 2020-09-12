n,m = map(int, input().split())
al = list(map(int, input().split()))

num_to_hon = [0, 2,5,5,4,5,6,3,7,6]
hon_to_num_dic = {}
for a in al:
    hon = num_to_hon[a]
    hon_to_num_dic.setdefault(hon,0)
    hon_to_num_dic[hon] = max(a, hon_to_num_dic[hon])


dp = [{'keta':0, 'num_cnts':[0]*10} for _ in range(n+10)]
for hon, num in hon_to_num_dic.items():
    dp[hon]['keta'] = 1
    dp[hon]['num_cnts'][num] += 1


for i in range(n):
    i_keta = dp[i]['keta']
    if i_keta == 0: continue
    for hon, num in hon_to_num_dic.items():
        i_num_cnts = dp[i]['num_cnts'][:]
        i_keta = dp[i]['keta']
        i_num_cnts[num] += 1
        next_dp = {'keta': i_keta+1, 'num_cnts':i_num_cnts[:]}
        # if i_keta == 0 and dp[i+hon]['keta'] > 0:
        #     continue
        if next_dp['keta'] > dp[i+hon]['keta']:
            dp[i+hon] = next_dp
            # print()
        elif next_dp['keta'] == dp[i+hon]['keta']:
            for comp_num in range(9,0,-1):
                if i_num_cnts[comp_num] > dp[i+hon]['num_cnts'][comp_num]:
                    dp[i+hon] = next_dp
                    break
                elif  i_num_cnts[comp_num] < dp[i+hon]['num_cnts'][comp_num]:
                    break


ans = []
for num in range(9,0,-1):
    ans.extend([str(num)]*dp[n]['num_cnts'][num])

print(''.join(ans))