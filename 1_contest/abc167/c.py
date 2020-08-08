INF = 99999999999

n, m, x = map(int, input().split()) 
c_l = []
a_l = []

for _ in range(n):
    a_list = list(map(int, input().split())) 
    c_l.append(a_list[0])
    a_l.append(a_list[1:])

min_c = INF
for i in range(2 ** n):
    bag_c = []
    bag_a = []
    for j in range(n):
        if ((i >> j) & 1):  
            bag_c.append(c_l[j])  
            bag_a.append(a_l[j])
        l = len(bag_a)
        c_sum = 0
        s_sum = [0]*m
        for ii in range(l):
            c_sum += bag_c[ii]
            for mm in range(m):
                s_sum[mm] += bag_a[ii][mm]
        if min(s_sum) >= x and c_sum < min_c:
            min_c = c_sum
if min_c == INF:
    print(-1)
else:   
    print(min_c)