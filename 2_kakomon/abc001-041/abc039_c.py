s=input()
wb='WBWBWWBWBWBW'*3
d={0:'Do',2:'Re',4:'Mi',5:'Fa',7:'So',9:'La',11:'Si'}
for i in range(12):
    if s[:20]==wb[i:i+20]:
        print(d[i])
        exit()