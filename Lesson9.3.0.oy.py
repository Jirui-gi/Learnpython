Info = { "Name": "Xiao", "Age":18,"Math score":87, "Physic score": 89,"Chemistry score": 90}
x = [Info["Math score"],Info["Physic score"],Info["Chemistry score"]]
a = x[0]
b = x[0]
for i in range (len(x)):
    if a < x[i]:
        a = x[i]
    if b > x[i]:
        b=x[i]
c = None 
d = None
for y,z in Info.items():
    if z == a:
        c = y
    if z == b:
        d = y
print(f"Highest subject: {c}: {a}\nLowest subject: {d}: {b}")


