ds=[
    'N','NNE','NE',
    'ENE','E','ESE',
    'SE','SSE','S','SSW','SW',
    'WSW','W','WNW','NW','NNW'
]

ws=[24,154,334,544,794,1074,1384,1714,2074,2444,2844,3264]

dire,dis=map(int, input().split())
ansd='N'
for i in range(16):
    if dire<i*225+113:
        ansd=ds[i]
        break
answ=12
dis=(dis*100)//60
for i,w in enumerate(ws):
    if dis<=w:
        answ=i
        break

if answ==0:ansd='C'

print(ansd,answ)
