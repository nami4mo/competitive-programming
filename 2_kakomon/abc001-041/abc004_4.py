r,g,b=map(int, input().split())

ans = 10**18
for gl in range(-500,500):
    gr = gl+g
    if gl<=-99:
        rc = r*(r-1)//2
        rc += (abs(gl)-99)*r
    else:
        half = min(gl+99,r//2)
        half_rem = r-1-half
        rc = half*(half+1)//2 + half_rem*(half_rem+1)//2
    
    if gr <= 0:
        gc = g*(g-1)//2
        gc += (abs(gr)+1)*g
    elif gl >= 0:
        gc = g*(g-1)//2
        gc += abs(gl)*g
    else:
        gc = abs(gl)*(abs(gl)+1)//2 + gr*(gr-1)//2

    if gr>=100:
        bc = b*(b-1)//2
        bc += (gr-100)*b
    else:
        half = min(100-gr,b//2)
        half_rem = b-1-half
        bc = half*(half+1)//2 + half_rem*(half_rem+1)//2

    v = rc+gc+bc
    # if v==5:
    #     print(gl,gr)
    #     print(rc,gc,bc)
    ans = min(ans,v)
print(ans)