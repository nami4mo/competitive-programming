import math
a, b, h, m = map(int, input().split()) 


min_sum = 60 * h + m
h_d = math.radians(90 - 360*min_sum/720)
m_d = math.radians(90 - 360*m/60)

h_x = a*math.cos(h_d)
h_y = a*math.sin(h_d)

m_x = b*math.cos(m_d)
m_y = b*math.sin(m_d)

d2 = (h_x-m_x)**2 + (h_y-m_y)**2
ans = d2**0.5
print(ans)