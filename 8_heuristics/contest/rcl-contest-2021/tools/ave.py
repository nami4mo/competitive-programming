import sys

filename=sys.argv[1]
vals=[]
with open(filename, 'r') as f:
    vals = f.read().rstrip().split('\n')

# print(vals)
vals=list(map(int,vals))
ave=sum(vals)//len(vals)

print(ave)

ave=f'[{ave}]'
vals=list(map(str,vals))
vals=[ave]+vals

with open(filename, 'w', newline='\n') as f:
    for v in vals: f.write(v+'\n')
