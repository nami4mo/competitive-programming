# 今日はおやすみです　

n=int(input())
al=list(map(int, input().split()))
bl=list(map(int, input().split()))
pl=list(map(int, input().split())) # i have pl[i]
pl=[p-1 for p in pl]
have_i=[-1]*n # i belongs to have_i[i]
for i in range(n):
    have_i[pl[i]]=i

for i in range(n):
    if i!=pl[i] and al[i]<=bl[pl[i]]:
        print(-1)
        exit()

aal=[(a,i) for i,a in enumerate(al)]
aal.sort()
ansl=[]
for a, aind in aal:
    if aind==pl[aind]:continue
    swaped=have_i[aind]
    have_i[pl[aind]]=swaped
    pl[swaped]=pl[aind]
    ansl.append((aind+1,swaped+1))

print(len(ansl))
for a,b in ansl:print(a,b)