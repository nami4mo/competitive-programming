s = input()
n = len(s)
rem2019 = [0]*2019
rem2019[0] = 1
curr_rem = 0
ans = 0
for i in range(n-1,-1,-1):
    ten = pow(10, n-1-i, 2019)
    curr_rem = curr_rem + ten*int(s[i])
    curr_rem%=2019
    ans += rem2019[curr_rem]
    rem2019[curr_rem]+=1

print(ans)