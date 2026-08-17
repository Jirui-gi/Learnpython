yourlist =[]
b=int(input("How  many number?:"))
for k in range (b):
    a = int(input("Enter a number:"))
    yourlist.append(a)
def analyze_numbers(number):
    x = number[0]
    y = number[0]
    z=0
    t=0
    for i in range (len(number)):
        if x< number[i]:
            x = number[i]
        if y > number[i]:
            y = number[i]
        z += number[i]
        if number[i]%2==0:
            t+=1
    z= z/len(number)
    return x,y,z,t
m,n,p,q = analyze_numbers(yourlist)
print("Max:",m)
print("Min",n)
print("Average:",p)
print("Even number:",q)