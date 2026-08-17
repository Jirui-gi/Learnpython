
def calculate_average(number):
    sum = 0
    for i in range(5):
        sum += number[i]
    sum = sum/5
    return sum
numbers= [10,20,30,40,50]
print("Value:", calculate_average(numbers))
    
        

