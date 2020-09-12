def add_list(l1,l2):
    res = []
    for v1,v2 in zip(l1,l2):
        res.append(v1+v2)
    return res

def sub_list(l1,l2):
    res = []
    for v1,v2 in zip(l1,l2):
        res.append(v1-v2)
    return res

n = int(input())
al = list(map(int, input().split()))
al2 = []
for a in al:
    a2 = list( map(int,format(a,'020b')) )
    al2.append(a2)

# print(al2)

left = -1
right = -1
next_i = 0
each_keta = [0]*20
ans = 0
while True:
    if right == n-1:
        break
    next_2 = add_list(al2[right+1], each_keta)
    if 2 in next_2:
        left += 1
        each_keta = sub_list(each_keta, al2[left])
    else:
        right += 1
        each_keta = next_2[:]
        ans += (right-left)

print(ans)