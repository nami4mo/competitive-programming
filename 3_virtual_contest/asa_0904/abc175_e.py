r,c,k = map(int, input().split())
rckl = [ [0]*c for _ in range(r) ]

for _ in range(k):
    r_,c_,v_ = map(int, input().split())
    rckl[r_-1][c_-1] = v_

dp0 = [ [0]*c for _ in range(r) ]
dp1 = [ [0]*c for _ in range(r) ]
dp2 = [ [0]*c for _ in range(r) ]
dp3 = [ [0]*c for _ in range(r) ]


dp1[0][0] = rckl[0][0]

for i in range(r):
    for j in range(c):
        if j+1 < c: 
            dp0[i][j+1] = max(dp0[i][j], dp0[i][j+1]) 
            dp1[i][j+1] = max(dp1[i][j], dp1[i][j+1]) 
            dp2[i][j+1] = max(dp2[i][j], dp2[i][j+1]) 
            dp3[i][j+1] = max(dp3[i][j], dp3[i][j+1]) 
            if rckl[i][j+1] > 0:
                v = rckl[i][j+1] 
                dp1[i][j+1] = max(dp1[i][j+1], dp0[i][j] + v)
                dp2[i][j+1] = max(dp2[i][j+1], dp1[i][j] + v)
                dp3[i][j+1] = max(dp3[i][j+1], dp2[i][j] + v)

        if i+1 < r: 
            dp0[i+1][j] = max(dp0[i][j], dp1[i][j], dp2[i][j], dp3[i][j], dp0[i+1][j]) 
            if rckl[i+1][j] > 0:
                v = rckl[i+1][j] 
                dp1[i+1][j] = max(dp1[i+1][j], dp0[i][j]+v, dp1[i][j]+v, dp2[i][j]+v, dp3[i][j]+v)


ans = max(dp0[-1][-1], dp1[-1][-1], dp2[-1][-1], dp3[-1][-1])
print(ans)
