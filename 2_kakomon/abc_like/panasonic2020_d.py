
def dfs(s,last,n,ansl):
    if len(s) == n:
        ansl.append(s)
        return
    for i in range(last+2):
        dfs(s+[i], max(last,i),n,ansl)

n = int(input())
ansl = []
dfs([0],0,n,ansl)
# print(ansl)

for ans in ansl:
    s = ''
    for a in ans:
        s += chr(ord('a')+a)
    print(s)