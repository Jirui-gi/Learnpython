mylist = [12,7,25,3,18]
def analyze_numbers(number):
    a = mylist[0]
    b = mylist[0]
    c = 0
    for i in range (len(number)):
        if a < mylist[i]:
            a= mylist[i]
        if b > mylist[i]:
            b = mylist[i]
        c += mylist[i]
    c = c/len(number)
    return a,b,c  
print(analyze_numbers(mylist))



