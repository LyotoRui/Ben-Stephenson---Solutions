import math

t1 = math.radians(float(input()))
g1 = math.radians(float(input()))
t2 = math.radians(float(input()))
g2 = math.radians(float(input()))

distance = 6371.01 * math.acos(math.sin(t1)*math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))

print(distance)
