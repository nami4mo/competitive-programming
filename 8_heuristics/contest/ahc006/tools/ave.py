import sys

filename=sys.argv[1]
vals=[]
with open(filename, 'r') as f:
    vals = f.read().rstrip().split('\n')

scores=[]
for row in vals:
    row=row.split()
    if 'score:' in row[0]:
        scores.append(int(row[1]))

ave=sum(scores)//len(scores)

ave=f'[{ave}]'
scores=list(map(str,scores))
scores=[ave]+scores

with open(filename+'.ave.txt', 'w', newline='\n') as f:
    for v in scores: f.write(v+'\n')
