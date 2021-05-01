s=input()
for i in range(8):
    if i==3:
        if s[i]!='-':break
    else:
        if not ord('0')<=ord(s[i])<=ord('9'):break
else:
    print('Yes')
    exit()
print('No')