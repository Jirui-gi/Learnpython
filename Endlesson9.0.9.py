a = {"Math": 100,"Physic": 85,"Biology": 56,"History": 49,"Data science":98}
b = [a["Math"],a["Physic"],a["Biology"],a["History"],a["Data science"]]
x = b[0]
y = b[0]
for i in range(len(b)):
    if x < b[i]:
        x = b[i]
    if y > b[i]:
        y = b[i]
c = None
d = None
for k,v in a.items():
    if v == x:
        c = k
    if v == y:
        d = k
t =0
for u in range (len(b)):
    t += b[u]
t = t/len(b)
print(f"{c}: {x}\n{d}: {y}\nAverage: {t}")

