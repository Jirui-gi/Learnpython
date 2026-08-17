a = []

for i in range(1, 901):
    student = {
        "Name": f"Student_{i}",
        "Age": 15,
        "Math": (i * 17) % 101,
        "Physic": (i * 23) % 101,
        "Chemistry": (i * 31) % 101
    }
    a.append(student)
h= {}
def average(a,b,c):
    (a+b+c)/3
    return (a+b+c)/3
for i in a:
    o=average(i["Math"],i["Physic"],i["Chemistry"])
    h[i["Name"]] = o
n =None
r= None
good = 0
bad = 0
j = 0
for k,v in h.items():
    if good< v:
        good = v
        n = k
    if bad>v:
        bad = v
        r =k
    if v>=80:
        j += 1
print(f"Highest score: {n}-{good}\nLowest score: {r}-{bad}\nNumber of student's score: {j} ")       

    

    
        
    




    

    
    
 