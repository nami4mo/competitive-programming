s = input()
if 'W' in s and 'E' in s and 'N' in s and 'S' in s:
    print('Yes')
elif 'W' in s and 'E' in s and not 'N' in s and not 'S' in s:
    print('Yes')
elif not 'W' in s and not 'E' in s and 'N' in s and 'S' in s:
    print('Yes')
else:
    print('No')
