ansl = []
for _ in range(int(input())):
    x,y,k = map(int, input().split())
    need = y*k+k
    need_add = ((need-1)-1)//(x-1) + 1
    ans = need_add + k
    ansl.append(ans)

for ans in ansl: print(ans)