Info  = {
    "Name": "Xiao",
    "Age": 18,
    "Math score": 36,
    "Physic score": 18,
    "Chemistry score": 67,
}
A= [Info["Math score"], Info["Physic score"],Info["Chemistry score"]]
c= A[0]
b = A[0]
for i in range(len(A)):
    if b < A[i]:
        b = A[i]
    if c > A[i]:
        c = A[i]
print(f"Maximum: {b}\nMinimum: {c}")

    


    
    
    
    
    
    





