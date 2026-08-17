def find_max(number):
    x = number[0]
    for i in range(len(number)):
        if x < number[i]:
            x = number[i]
    return x 
num_bers = [65,47,30,98,90]
print("Maximum:", find_max(num_bers))