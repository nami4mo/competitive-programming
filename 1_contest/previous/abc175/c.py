x,k,d = map(int, input().split())
x = abs(x)

if x > k*d:
    ans = x- k*d
    print(ans)
    exit()

p_min_cnt = x//d
rem = k - p_min_cnt
p_min = x%d

if rem%2 == 0:
    print(p_min)
else:
    m_min = abs(p_min-d)
    print(m_min)