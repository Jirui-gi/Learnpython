b = {"Name": "Tao","Age":15,"Math" : 86,"Physic": 88,"Chemistry":77}
c = {"Name": "Xiao","Age":15,"Math" : 56,"Physic": 48,"Chemistry":79}
d = {"Name": "Tiao","Age":15,"Math" : 80,"Physic": 98,"Chemistry":73}
e = {"Name": "Yao","Age":15,"Math" : 97,"Physic": 88,"Chemistry":100}
f = {"Name": "Mao","Age":15,"Math" : 64,"Physic": 82,"Chemistry":45}
a = [b,c,d,e,f]
y = []
t =[]
r= []
x = None
p = 0
name = None
noo = None
def average(m,n,p):
    (m+n+p)/3
    return (m+n+p)/3
for i in a:
    print(f"Name: {i['Name']}| Age: {i['Age']}| Math: {i['Math']}| Physic: {i['Physic']}| Chemistry: {i['Chemistry']}")
for k in range(len(a)):
    x= average(a[k]["Math"],a[k]["Physic"],a[k]["Chemistry"])
    y.append(x)
    t.append(a[k]["Name"])
    print(f"{a[k]['Name']}-Average: {x}")
z =y[0]
o = y[0]
for  u in range(len(y)):
    if z < y[u]:
        z = y[u]
        name = t[u]
    if o > y[u]:
        o= y[u]
        noo = t[u]
    if y[u] >= 80:
        r.append(t[u])
        p+= 1
print(f"Highest Average: {name}-{z}")
print(f"Lowest Average: {noo}-{o}")
print(f"High Achieving student: {r}")
print(f"Number of high achieving student: {p}")


        
    




