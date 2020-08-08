n,a,b = map(int, input().split())
diff = abs(a-b)

if diff%2 == 0:
    print(diff//2)
    exit()

adiff = min( abs(a-1), abs(n-a) )
bdiff = min( abs(b-1), abs(n-b) )
mdiff = min(adiff,bdiff)

ans = mdiff + 1 + diff//2
print(ans)