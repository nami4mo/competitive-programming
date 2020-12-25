s=input()
alp_d = {chr(ord('a') + i): False for i in range(26)}

if s=='zyxwvutsrqponmlkjihgfedcba':
    print(-1)
    exit()

s=list(s)


for si in s:
    alp_d[si]=True 

if len(s)!=26:
    for k,v in alp_d.items():
        if not v:
            s.append(k)
            print(''.join(s))
            exit()


alp_d[s[-1]]=False
for i in range(26-2,-1,-1):
    si = s[i]
    for j in range(1,26):
        sii = chr(ord(si)+j)
        if sii>'z':break
        if not alp_d[sii]:
            s = s[:i]+[sii]
            print(''.join(s))
            exit()
    alp_d[si]=False