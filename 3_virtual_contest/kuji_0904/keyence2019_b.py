s=input()
rem = len(s)-7

if s[rem:] == 'keyence': 
    print('YES')
    exit()
for i in range(8):
    news = s[0:i] + s[i+rem:]
    if news == 'keyence':
        print('YES')
        break
else:
    print('NO')