s = input()
s = s[::-1]
n = len(s)

# stmp = s[::-1]
# for i in range(len(s)):
#     for j in range(i,len(s)):
#         sint = int(stmp[i:j+1])
#         if sint % 2019 == 0: 
#             print(n-j,n-i)
#             print(sint)
#             print()


rem2019_cnts = [0]*2019
rem2019_cnts[0] = 1
curr_rem = int(s[0])
rem2019_cnts[curr_rem] = 1
curr_10_rem = 1
ans = 0
for i,si in enumerate(s[1:]):
    sint = int(si)

    next_10_rem = (curr_10_rem*10)%2019
    next_rem = (next_10_rem*sint + curr_rem)%2019

    ans += rem2019_cnts[next_rem]
    rem2019_cnts[next_rem] += 1
    
    curr_10_rem = next_10_rem
    curr_rem = next_rem
    # print(i+2, curr_rem)

print(ans)