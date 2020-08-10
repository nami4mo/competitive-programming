s = input()
for i in range(2000):
    s = s.replace('  ',' ')

s = s.replace(' ',',')
print(s)