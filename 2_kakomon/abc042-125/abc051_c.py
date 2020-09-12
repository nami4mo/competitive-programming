sx,sy,tx,ty = map(int, input().split())
x = tx-sx
y = ty-sy

ans = []
ans = ans + ['R']*x
ans = ans + ['U']*y

ans = ans + ['L']*x
ans = ans + ['D']*y

ans = ans + ['D']
ans = ans + ['R']*(x+1)
ans = ans + ['U']*(y+1)
ans = ans + ['L']

ans = ans + ['U']
ans = ans + ['L']*(x+1)
ans = ans + ['D']*(y+1)
ans = ans + ['R']

print(''.join(ans))
