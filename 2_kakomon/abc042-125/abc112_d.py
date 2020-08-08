import bisect

n,m = map(int, input().split())

n_facs_s = []
n_facs_l = []
for i in range(1, int(-(-m**0.5//1))+1):
    if m%i == 0:
        n_facs_s.append(i)
        n_facs_l.append(m//i)


n_faces = n_facs_s + n_facs_l[::-1]
ind = bisect.bisect_right(n_faces, n)
if n_faces[ind-1] == n:
    ind-=1
print(m//n_faces[ind])
