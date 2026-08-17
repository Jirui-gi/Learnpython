numbers = [65,47,30,98,80]
x = numbers[0]
for i in range(len(numbers)):
    if x > numbers[i]:
        x = numbers[i]
print(" Min:", x)

