s=input()
t=input()
ans = 10**9
for i in range(len(s)):
    # print('---',i)
    val = 0
    for j in range(len(t)):
        if i+j >= len(s):
            break
        si = s[i+j]
        ti = t[j]
        # print(si,ti)
        if si != ti:  val += 1
    else:
        ans = min(ans,val)

print(ans)