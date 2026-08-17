numbers = []
for i in range (5):
     a = int(input("Enter a number:"))
     numbers.append(a)
b = numbers[0]
for k in range (1,5):
    if b < numbers[k]:
        b = numbers[k]
print("Max:", b)
    
    