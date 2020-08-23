n = int(input())
s = input()
q = int(input())
kl = list(map(int, input().split()))
ansl = []
for k in kl:
    d_cnt = 0
    m_cnt = 0
    c_cnt = 0
    dm_cnt = 0
    dmc_cnt = 0
    for i in range(k):
        si = s[i]
        if si == 'D':
            d_cnt += 1
        elif si == 'M':
            m_cnt += 1
            dm_cnt += d_cnt
        elif si == 'C':
            c_cnt += 1
            dmc_cnt += dm_cnt   
    
    rem = n-k
    for i in range(rem):
        drop = s[i]
        new = s[i+k]
        if drop == 'D':
            d_cnt -= 1
            dm_cnt -= m_cnt
        elif drop == 'M':
            m_cnt -= 1
        elif drop == 'C':
            c_cnt -= 1
        
        if new == 'D':
            d_cnt += 1
        elif new == 'M':
            m_cnt += 1
            dm_cnt += d_cnt
        elif new == 'C':
            c_cnt += 1
            dmc_cnt += dm_cnt

    ansl.append(dmc_cnt)

for a in ansl: print(a)