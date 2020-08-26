n = int(input())
five = n//5
six = five%6
rem = n%5
ll = []
for i in range(6-six):
    ll.append(six+1+i)
for i in range(six):
    ll.append(i+1)

for i in range(rem):
    ll[i], ll[i+1] = ll[i+1], ll[i]

ll = map(str,ll)
ans = ''.join(ll)
print(ans)