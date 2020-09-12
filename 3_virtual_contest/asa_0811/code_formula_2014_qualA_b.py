a,b = map(int, input().split())
pl = list(map(int, input().split()))
ql = list(map(int, input().split()))

ans = ['']*11
for i in range(10):
    if i in pl:
        ans[i] = ('. ')
    elif i in ql:
        ans[i] = ('o ')
    else:
        ans[i] = ('x ')
ans[10] = ans[0]

print(''.join(ans[7:11]))
print(' ' + ''.join(ans[4:7]))
print('  ' + ''.join(ans[2:4]))
print('   ' + ans[1])
